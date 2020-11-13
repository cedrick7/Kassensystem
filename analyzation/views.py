from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from analyzation.forms import *
from cashbox.forms import *
from product.models import *
from django.db.models import Sum
from django.db import connection
from cashbox.models import Cashbox
from collections import namedtuple
from datetime import datetime, timedelta
import datetime
import datetime, json, re

# -------------------------------------------------------------------------
# analyzation

# who can access:
# --> analyzation only
# what i need:
# a list of all the


# -------------------------------------------------------------------------

#############################################################
#Views

# RawSQL
def raw_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]


# DashboardView
def analyzation_dashboard_view(request, *args, **kwargs):
    global sales_day, sales_week, sales_month, sales_product, sales_dienst, cashbox, revenue_products_data, revenue_services_data, revenue_total_data, revenue_chart_x_axes
    global revenue_chart_y_axes, revenue_chart_legend, revenue_products_legend, revenue_services_legend, revenue_total_legend, products_chart_labels, products_data
    global products_chart_x_axes, products_chart_y_axes, services_data, services_chart_labels, services_chart_x_axes, services_chart_y_axes, services_chart_legend
    global date_begin, date_end
    context = {}

    if request.method == 'GET':
        dateRange_form = FormDashboard()

        #Alle Kassen
        cashbox = Cashbox.objects.all()
        #Tägliche Einnahmen
        query = "SELECT SUM(totalcosts) AS Summe FROM cashbox_bill \
                WHERE creation >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY) AND creation <= CURRENT_TIMESTAMP();" #between statement geht nicht
        result = raw_sql(query)
        sales_day = result[0].Summe

        #Wöchentliche Einnahmen
        query = "SELECT SUM(totalcosts) AS Summe FROM cashbox_bill \
                WHERE creation >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY) AND creation <= CURRENT_TIMESTAMP();" #between statement geht nicht
        result = raw_sql(query)
        sales_week = result[0].Summe

        #Monatliche Einnahmen
        query = "SELECT SUM(totalcosts) AS Summe FROM cashbox_bill \
                WHERE creation >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY) AND creation <= CURRENT_TIMESTAMP();" #between statement geht nicht
        result = raw_sql(query)
        sales_month = result[0].Summe

        ##Einnahmen Produkte
        query = "SELECT SUM(costs) AS 'Summe' FROM 07yp3juew2.cashbox_bill AS bills JOIN 07yp3juew2.cashbox_bill_product AS products \
                  ON bills.id = products.bill_id INNER JOIN 07yp3juew2.product_product AS product ON products.product_id = product.id \
                  WHERE creation >= DATE_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 DAY) \
                  AND type='PR';" 
        query_result = raw_sql(query)
        sales_product = query_result[0].Summe
        ##Einnahmen Dienstleistungen
        query = "SELECT SUM(costs) AS 'Summe' FROM 07yp3juew2.cashbox_bill AS bills JOIN 07yp3juew2.cashbox_bill_product AS products \
                ON bills.id = products.bill_id INNER JOIN 07yp3juew2.product_product AS product ON products.product_id = product.id \
                WHERE creation >= DATE_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 DAY) \
                AND type='DI';" 
        query_result = raw_sql(query)
        sales_dienst = query_result[0].Summe

        #Standarddaten
        ## chart no.1 - Umsatz Überblick [line-chart] ##
        #Dynamische Werte
        query = "SELECT WEEKDAY(DATE(creation)) AS Wochentag, SUM(totalcosts) AS Summe, pp.type AS Typ \
                FROM cashbox_bill AS cb INNER JOIN cashbox_bill_product AS cbp ON cb.id = cbp.bill_id \
                INNER JOIN product_product AS pp ON cbp.product_id = pp.id \
                WHERE creation >= date_sub(current_timestamp(), INTERVAL 7 DAY) \
                AND creation <= current_timestamp() \
                GROUP BY Wochentag, Typ \
                ORDER BY Wochentag DESC;"
        query_result = raw_sql(query)
        query2 = "SELECT WEEKDAY(DATE(creation)) AS Wochentag, SUM(totalcosts) AS Summe \
                 FROM cashbox_bill AS cb INNER JOIN cashbox_bill_product AS cbp ON cb.id = cbp.bill_id \
                 INNER JOIN product_product AS pp ON cbp.product_id = pp.id \
                 WHERE creation >= date_sub(current_timestamp(), INTERVAL 7 DAY) \
                 AND creation <= current_timestamp() \
                 GROUP BY Wochentag \
                 ORDER BY Wochentag DESC;"
        query2_result = raw_sql(query2)
        
        revenue_products_data = []
        revenue_services_data = []
        revenue_total_data = []
        #Festwerte
        revenue_chart_x_axes = 'Zeit in Tagen'
        revenue_chart_y_axes = 'Umsatz in €'
        revenue_chart_legend = 'Umsatz'
        revenue_products_legend = 'Produkte'
        revenue_services_legend = 'Dienstleistungen'
        revenue_total_legend = 'Gesamt'
        #Dynamische Werte füllen
        for i in query_result:
            if i.Wochentag == 0:
                tmp = "Montag"
            elif i.Wochentag == 1:
                tmp = "Dienstag"
            elif i.Wochentag == 2:
                tmp = "Mittwoch"
            elif i.Wochentag == 3:
                tmp = "Donnerstag"
            elif i.Wochentag == 4:
                tmp = "Freitag"
            elif i.Wochentag == 5:
                tmp = "Samstag"
            elif i.Wochentag ==6:
                tmp = "Sonntag"

            if i.Typ == "PR":
               revenue_products_data.append([tmp,i.Summe]) 
            elif i.Typ == "DI":
                revenue_services_data.append([tmp,i.Summe])
        
        for i in query2_result:
            if i.Wochentag == 0:
                revenue_total_data.append(["Montag",i.Summe])
            elif i.Wochentag == 1:
                revenue_total_data.append(["Dienstag",i.Summe])
            elif i.Wochentag == 2:
                revenue_total_data.append(["Mittwoch",i.Summe])
            elif i.Wochentag == 3:
                revenue_total_data.append(["Donnerstag",i.Summe])
            elif i.Wochentag == 4:
                revenue_total_data.append(["Freitag",i.Summe])
            elif i.Wochentag == 5:
                revenue_total_data.append(["Samstag",i.Summe])
            elif i.Wochentag ==6:
                revenue_total_data.append(["Sonntag",i.Summe])

        ## chart no.2 - Produkte Überblick (TOP-5 Ranking) [bar-chart] ##
        query = "SELECT product.description AS Produkt, SUM(DISTINCT(amount)) AS Summe \
                FROM product_product AS product INNER JOIN cashbox_bill_product AS products \
                ON product.id = products.product_id  \
                GROUP BY(description) \
                ORDER BY Summe ASC \
                LIMIT 5;"

        #Dynamische Werte
        query_result = raw_sql(query)
        products_chart_labels = []
        products_data = []

        #Festwerte
        products_chart_x_axes = 'Produkte'
        products_chart_y_axes = 'Anzahl der Verkäufe pro Produkt'

        #Dynamische Werte füllen
        for i in query_result:
            products_chart_labels.append(i.Produkt)
            products_data.append(i.Summe)
        
        ## chart no.3 - Dienstleistungen Überblick (TOP-X Ranking) [bar-chart] ##
        query = "SELECT pc.title AS Kategorie, SUM(cbp.amount) AS Summe \
                FROM product_category AS pc \
                INNER JOIN product_product_category AS ppc ON pc.id = ppc.category_id \
                INNER JOIN product_product AS pp ON ppc.product_id = pp.id \
                INNER JOIN cashbox_bill_product AS cbp ON pp.id = cbp.product_id \
                GROUP BY (pc.title) \
                ORDER BY Summe DESC \
                LIMIT 5;"          
        #Dynamische Werte
        query_result = raw_sql(query)
        services_data = []
        services_chart_labels = []
        #Festwerte
        services_chart_x_axes = 'Kategoriename'
        services_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'
        services_chart_legend = 'TOP 5 Dienstleistungen'
        #Dynamische Werte füllen
        for i in query_result:
            services_data.append(i.Summe)
            services_chart_labels.append(i.Kategorie)
        


        #Context
        context = {'form': dateRange_form,
                   'sales_day' : sales_day,
                   'sales_week' : sales_week,
                   'sales_month' : sales_month,
                   'sales_product': sales_product,
                   'sales_dienst': sales_dienst,
                   'cashbox' : cashbox,
                   # chart no.1 - Umsatz Überblick [line-chart]
                   'revenue_products_data' : revenue_products_data,
                   'revenue_services_data' : revenue_services_data,
                   'revenue_total_data' : revenue_total_data,
                   'revenue_chart_x_axes' : revenue_chart_x_axes,
                   'revenue_chart_y_axes' : revenue_chart_y_axes,
                   'revenue_chart_legend' : revenue_chart_legend,
                   'revenue_products_legend' : revenue_products_legend,
                   'revenue_services_legend' : revenue_services_legend,
                   'revenue_total_legend' : revenue_total_legend,
                   #chart no.2 - Produkte Überblick (TOP-5 Ranking) [bar-chart]
                   'products_chart_labels' : products_chart_labels,
                   'products_data' : products_data,
                   'products_chart_x_axes' : products_chart_x_axes,
                   'products_chart_y_axes' : products_chart_y_axes,
                   # chart no.3 - Dienstleistungen Überblick (TOP-X Ranking) [bar-chart]
                   'services_data' : services_data,
                   'services_chart_labels' : services_chart_labels,
                   'services_chart_x_axes' : services_chart_x_axes,
                   'services_chart_y_axes' : services_chart_y_axes,
                   'services_chart_legend' : services_chart_legend,
                  }
    
    elif request.method == 'POST':
        dateRange_form = FormDashboard(request.POST)

        if request.POST.get("mstzfltr"):
            print("Umsatzfilter")
            date = str(dateRange_form.data["dateRange"])
            dates = date.split(" - ")
            date_begin = datetime.datetime.strptime(dates[0], '%d.%m.%Y')
            date_end = datetime.datetime.strptime(dates[1], '%d.%m.%Y')
            ## chart no.1 - Umsatz Überblick [line-chart] ##
            #Dynamische Werte
            query = "SELECT WEEKDAY(DATE(creation)) AS Wochentag, SUM(totalcosts) AS Summe, pp.type AS Typ \
                    FROM cashbox_bill AS cb INNER JOIN cashbox_bill_product AS cbp ON cb.id = cbp.bill_id \
                    INNER JOIN product_product AS pp ON cbp.product_id = pp.id \
                    WHERE creation > '" + str(date_begin) + "' \
                    AND creation < '" + str(date_end) + "' \
                    GROUP BY Wochentag, Typ \
                    ORDER BY Wochentag DESC;"
            query_result = raw_sql(query)
            query2 = "SELECT WEEKDAY(DATE(creation)) AS Wochentag, SUM(totalcosts) AS Summe \
                    FROM cashbox_bill AS cb INNER JOIN cashbox_bill_product AS cbp ON cb.id = cbp.bill_id \
                    INNER JOIN product_product AS pp ON cbp.product_id = pp.id \
                    WHERE creation > '" + str(date_begin) + "' \
                    AND creation < '" + str(date_end) + "' \
                    GROUP BY Wochentag \
                    ORDER BY Wochentag DESC;"
            query2_result = raw_sql(query2)
            revenue_products_data = []
            revenue_services_data = []
            revenue_total_data = []
            #Festwerte
            revenue_chart_x_axes = 'Zeit in Tagen'
            revenue_chart_y_axes = 'Umsatz in €'
            revenue_chart_legend = 'Umsatz'
            revenue_products_legend = 'Produkte'
            revenue_services_legend = 'Dienstleistungen'
            revenue_total_legend = 'Gesamt'
            #Dynamische Werte füllen
            for i in query_result:
                if i.Wochentag == 0:
                    tmp = "Montag"
                elif i.Wochentag == 1:
                    tmp = "Dienstag"
                elif i.Wochentag == 2:
                    tmp = "Mittwoch"
                elif i.Wochentag == 3:
                    tmp = "Donnerstag"
                elif i.Wochentag == 4:
                    tmp = "Freitag"
                elif i.Wochentag == 5:
                    tmp = "Samstag"
                elif i.Wochentag ==6:
                    tmp = "Sonntag"

                if i.Typ == "PR":
                    revenue_products_data.append([tmp,i.Summe]) 
                elif i.Typ == "DI":
                    revenue_services_data.append([tmp,i.Summe])
            
            for i in query2_result:
                if i.Wochentag == 0:
                    revenue_total_data.append(["Montag",i.Summe])
                elif i.Wochentag == 1:
                    revenue_total_data.append(["Dienstag",i.Summe])
                elif i.Wochentag == 2:
                    revenue_total_data.append(["Mittwoch",i.Summe])
                elif i.Wochentag == 3:
                    revenue_total_data.append(["Donnerstag",i.Summe])
                elif i.Wochentag == 4:
                    revenue_total_data.append(["Freitag",i.Summe])
                elif i.Wochentag == 5:
                    revenue_total_data.append(["Samstag",i.Summe])
                elif i.Wochentag ==6:
                    revenue_total_data.append(["Sonntag",i.Summe])


        elif request.POST.get("prdktfltr"):
            print("Produktfilter")
            limit = dateRange_form.data["radio"]
            if limit == "5":
                print("5")
                ## chart no.2 - Produkte Überblick (TOP-5 Ranking) [bar-chart] ##
                query = "SELECT product.description AS Produkt, SUM(DISTINCT(amount)) AS Summe \
                        FROM product_product AS product INNER JOIN cashbox_bill_product AS products \
                        ON product.id = products.product_id  \
                        GROUP BY(description) \
                        ORDER BY Summe ASC \
                        LIMIT 5;"

                #Dynamische Werte
                query_result = raw_sql(query)
                products_chart_labels = []
                products_data = []

                #Festwerte
                products_chart_x_axes = 'Produkte'
                products_chart_y_axes = 'Anzahl der Verkäufe pro Produkt'

                #Dynamische Werte füllen
                for i in query_result:
                    products_chart_labels.append(i.Produkt)
                    products_data.append(i.Summe)
        
            elif limit == "10":
                print("10")
                 ## chart no.2 - Produkte Überblick (TOP-10 Ranking) [bar-chart] ##
                query = "SELECT product.description AS Produkt, SUM(DISTINCT(amount)) AS Summe \
                        FROM product_product AS product INNER JOIN cashbox_bill_product AS products \
                        ON product.id = products.product_id  \
                        GROUP BY(description) \
                        ORDER BY Summe ASC \
                        LIMIT 10;"

                #Dynamische Werte
                query_result = raw_sql(query)
                products_chart_labels = []
                products_data = []

                #Festwerte
                products_chart_x_axes = 'Produkte'
                products_chart_y_axes = 'Anzahl der Verkäufe pro Produkt'

                #Dynamische Werte füllen
                for i in query_result:
                    products_chart_labels.append(i.Produkt)
                    products_data.append(i.Summe)

        elif request.POST.get("dnstlstngfltr"):
           print("Dienstleistungsfilter")
           limit = dateRange_form.data["radio"]
           if limit == "5":
                print("5")
                ## chart no.3 - Dienstleistungen Überblick (TOP-X Ranking) [bar-chart] ##
                query = "SELECT pc.title AS Kategorie, SUM(cbp.amount) AS Summe \
                        FROM product_category AS pc \
                        INNER JOIN product_product_category AS ppc ON pc.id = ppc.category_id \
                        INNER JOIN product_product AS pp ON ppc.product_id = pp.id \
                        INNER JOIN cashbox_bill_product AS cbp ON pp.id = cbp.product_id \
                        GROUP BY (pc.title) \
                        ORDER BY Summe DESC \
                        LIMIT 5;"          
                #Dynamische Werte
                query_result = raw_sql(query)
                services_data = []
                services_chart_labels = []
                #Festwerte
                services_chart_x_axes = 'Kategoriename'
                services_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'
                services_chart_legend = 'TOP 5 Dienstleistungen'
                #Dynamische Werte füllen
                for i in query_result:
                    services_data.append(i.Summe)
                    services_chart_labels.append(i.Kategorie)
        
           elif limit == "10":
                print("10")
                ## chart no.3 - Dienstleistungen Überblick (TOP-X Ranking) [bar-chart] ##
                query = "SELECT pc.title AS Kategorie, SUM(cbp.amount) AS Summe \
                        FROM product_category AS pc \
                        INNER JOIN product_product_category AS ppc ON pc.id = ppc.category_id \
                        INNER JOIN product_product AS pp ON ppc.product_id = pp.id \
                        INNER JOIN cashbox_bill_product AS cbp ON pp.id = cbp.product_id \
                        GROUP BY (pc.title) \
                        ORDER BY Summe DESC \
                        LIMIT 10;"          
                #Dynamische Werte
                query_result = raw_sql(query)
                services_data = []
                services_chart_labels = []
                #Festwerte
                services_chart_x_axes = 'Kategoriename'
                services_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'
                services_chart_legend = 'TOP 5 Dienstleistungen'
                #Dynamische Werte füllen
                for i in query_result:
                    services_data.append(i.Summe)
                    services_chart_labels.append(i.Kategorie)

        #context
        context = {'form': dateRange_form,
                   'sales_day' : sales_day,
                   'sales_week' : sales_week,
                   'sales_month' : sales_month,
                   'sales_product': sales_product,
                   'sales_dienst': sales_dienst,
                   'cashbox' : cashbox,
                   # chart no.1 - Umsatz Überblick [line-chart]
                   'revenue_products_data' : revenue_products_data,
                   'revenue_services_data' : revenue_services_data,
                   'revenue_total_data' : revenue_total_data,
                   'revenue_chart_x_axes' : revenue_chart_x_axes,
                   'revenue_chart_y_axes' : revenue_chart_y_axes,
                   'revenue_chart_legend' : revenue_chart_legend,
                   'revenue_products_legend' : revenue_products_legend,
                   'revenue_services_legend' : revenue_services_legend,
                   'revenue_total_legend' : revenue_total_legend,
                   #chart no.2 - Produkte Überblick (TOP-5 Ranking) [bar-chart]
                   'products_chart_labels' : products_chart_labels,
                   'products_data' : products_data,
                   'products_chart_x_axes' : products_chart_x_axes,
                   'products_chart_y_axes' : products_chart_y_axes,
                   # chart no.3 - Dienstleistungen Überblick (TOP-X Ranking) [bar-chart] 
                   'services_data' : services_data,
                   'services_chart_labels' : services_chart_labels,
                   'services_chart_x_axes' : services_chart_x_axes,
                   'services_chart_y_axes' : services_chart_y_axes,
                   'services_chart_legend' : services_chart_legend,
                  }
    return render(request, 'analyzation_dashboard.html', context)

# SalesView
def analyzation_sales_view(request, *args, **kwargs):
    global sales_product, sales_dienst, sales_month, sales_week, sales_day, cashbox, revenue_products_data, revenue_services_data, revenue_total_data, revenue_chart_x_axes
    global revenue_chart_y_axes, revenue_chart_legend, revenue_products_legend, revenue_services_legend, revenue_total_legend, products_chart_labels, products_data
    global products_chart_x_axes, products_chart_y_axes,services_data, services_chart_labels, services_chart_x_axes, services_chart_y_axes, services_chart_legend
    global payment_data, payment_chart_labels, payment_chart_legend, peak_times_data, peak_times_chart_labels, peak_times_chart_legend, peak_times_chart_x_axes
    
    context = {}
    # Globale Variablen, genutzt für GET und POST

    if request.method == 'GET':
        sales_form = FormSalesFilter() 

        #Alle Kassen
        cashbox = Cashbox.objects.all()
        #Tägliche Einnahmen
        query = "SELECT SUM(totalcosts) AS Summe FROM cashbox_bill \
                WHERE creation >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY) AND creation <= CURRENT_TIMESTAMP();" #between statement geht nicht
        result = raw_sql(query)
        sales_day = result[0].Summe

        #Wöchentliche Einnahmen
        query = "SELECT SUM(totalcosts) AS Summe FROM cashbox_bill \
                WHERE creation >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY) AND creation <= CURRENT_TIMESTAMP();" #between statement geht nicht
        result = raw_sql(query)
        sales_week = result[0].Summe

        #Monatliche Einnahmen
        query = "SELECT SUM(totalcosts) AS Summe FROM cashbox_bill \
                WHERE creation >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY) AND creation <= CURRENT_TIMESTAMP();" #between statement geht nicht
        result = raw_sql(query)
        sales_month = result[0].Summe

        ##Einnahmen Produkte
        query = "SELECT SUM(costs) AS 'Summe' FROM 07yp3juew2.cashbox_bill AS bills JOIN 07yp3juew2.cashbox_bill_product AS products \
                  ON bills.id = products.bill_id INNER JOIN 07yp3juew2.product_product AS product ON products.product_id = product.id \
                  WHERE creation >= DATE_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 DAY) \
                  AND type='PR';" 
        query_result = raw_sql(query)
        sales_product = query_result[0].Summe
        ##Einnahmen Dienstleistungen
        query = "SELECT SUM(costs) AS 'Summe' FROM 07yp3juew2.cashbox_bill AS bills JOIN 07yp3juew2.cashbox_bill_product AS products \
                ON bills.id = products.bill_id INNER JOIN 07yp3juew2.product_product AS product ON products.product_id = product.id \
                WHERE creation >= DATE_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 DAY) \
                AND type='DI';" 
        query_result = raw_sql(query)
        sales_dienst = query_result[0].Summe
        
        #Standarddaten
        ## chart no.1 - Umsatz Überblick [line-chart] ##
        #Dynamische Werte
        query = "SELECT WEEKDAY(DATE(creation)) AS Wochentag, SUM(totalcosts) AS Summe, pp.type AS Typ \
                FROM cashbox_bill AS cb INNER JOIN cashbox_bill_product AS cbp ON cb.id = cbp.bill_id \
                INNER JOIN product_product AS pp ON cbp.product_id = pp.id \
                WHERE creation >= date_sub(current_timestamp(), INTERVAL 7 DAY) \
                AND creation <= current_timestamp() \
                GROUP BY Wochentag, Typ \
                ORDER BY Wochentag ASC;"
        query_result = raw_sql(query)
        query2 = "SELECT WEEKDAY(DATE(creation)) AS Wochentag, SUM(totalcosts) AS Summe \
                 FROM cashbox_bill AS cb INNER JOIN cashbox_bill_product AS cbp ON cb.id = cbp.bill_id \
                 INNER JOIN product_product AS pp ON cbp.product_id = pp.id \
                 WHERE creation >= date_sub(current_timestamp(), INTERVAL 7 DAY) \
                 AND creation <= current_timestamp() \
                 GROUP BY Wochentag \
                 ORDER BY Wochentag ASC;"
        query2_result = raw_sql(query2)
        revenue_products_data = []
        revenue_services_data = []
        revenue_total_data = []
        #Festwerte
        revenue_chart_x_axes = 'Zeit in Tagen'
        revenue_chart_y_axes = 'Umsatz in €'
        revenue_chart_legend = 'Umsatz'
        revenue_products_legend = 'Produkte'
        revenue_services_legend = 'Dienstleistungen'
        revenue_total_legend = 'Gesamt'
        #Dynamische Werte füllen
        for i in query_result:
            if i.Wochentag == 0:
                tmp = "Montag"
            elif i.Wochentag == 1:
                tmp = "Dienstag"
            elif i.Wochentag == 2:
                tmp = "Mittwoch"
            elif i.Wochentag == 3:
                tmp = "Donnerstag"
            elif i.Wochentag == 4:
                tmp = "Freitag"
            elif i.Wochentag == 5:
                tmp = "Samstag"
            elif i.Wochentag ==6:
                tmp = "Sonntag"

            if i.Typ == "PR":
               revenue_products_data.append([tmp,float(i.Summe)])
            elif i.Typ == "DI":
                revenue_services_data.append([tmp,float(i.Summe)])
        
        for i in query2_result:
            if i.Wochentag == 0:
                revenue_total_data.append(["Montag",float(i.Summe)])
            elif i.Wochentag == 1:
                revenue_total_data.append(["Dienstag",float(i.Summe)])
            elif i.Wochentag == 2:
                revenue_total_data.append(["Mittwoch",float(i.Summe)])
            elif i.Wochentag == 3:
                revenue_total_data.append(["Donnerstag",float(i.Summe)])
            elif i.Wochentag == 4:
                revenue_total_data.append(["Freitag",float(i.Summe)])
            elif i.Wochentag == 5:
                revenue_total_data.append(["Samstag",float(i.Summe)])
            elif i.Wochentag ==6:
                revenue_total_data.append(["Sonntag",float(i.Summe)])

        print("\n===============================================================================================================")
        print("revenue_total_data: " , revenue_total_data)
        print("revenue_products_data: " , revenue_products_data)
        print("revenue_services_data: " , revenue_services_data)

        ## chart no.2 - Produkte Überblick (TOP-5 Ranking) [bar-chart] ##
        query = "SELECT product.description AS Produkt, SUM(DISTINCT(amount)) AS Summe \
                FROM product_product AS product INNER JOIN cashbox_bill_product AS products \
                ON product.id = products.product_id  \
                GROUP BY(description) \
                ORDER BY Summe ASC \
                LIMIT 5;"

        #Dynamische Werte
        query_result = raw_sql(query)
        products_chart_labels = []
        products_data = []

        #Festwerte
        products_chart_x_axes = 'Produkte'
        products_chart_y_axes = 'Anzahl der Verkäufe pro Produkt'

        #Dynamische Werte füllen
        for i in query_result:
            products_chart_labels.append(i.Produkt)
            products_data.append(float(i.Summe))

        ## chart no.3 - Dienstleistungen Überblick (TOP-X Ranking) [bar-chart] ##
        query = "SELECT pc.title AS Kategorie, SUM(cbp.amount) AS Summe \
                FROM product_category AS pc \
                INNER JOIN product_product_category AS ppc ON pc.id = ppc.category_id \
                INNER JOIN product_product AS pp ON ppc.product_id = pp.id \
                INNER JOIN cashbox_bill_product AS cbp ON pp.id = cbp.product_id \
                GROUP BY (pc.title) \
                ORDER BY Summe DESC \
                LIMIT 5;"          
        #Dynamische Werte
        query_result = raw_sql(query)
        services_data = []
        services_chart_labels = []
        #Festwerte
        services_chart_x_axes = 'Kategoriename'
        services_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'
        services_chart_legend = 'TOP 5 Dienstleistungen'
        #Dynamische Werte füllen
        for i in query_result:
            services_data.append(float(i.Summe))
            services_chart_labels.append(i.Kategorie)
        
        ## chart no.4 - Zahlungsmethoden [doughnut-chart] ##
        query = "SELECT cp.title AS Titel, (ROUND(COUNT(cp.id) / (SELECT COUNT(*) AS ges FROM cashbox_bill), 2) * 100) AS Summe \
                FROM cashbox_bill AS cb \
                INNER JOIN cashbox_paymenttool AS cp ON cb.paymenttool_id = cp.id \
                GROUP BY cp.title \
                LIMIT 5;"
        #Dynamische Werte
        query_result = raw_sql(query)
        payment_data = []
        payment_chart_labels = []
        #Festwerte
        payment_chart_legend = 'Zahlungsmethoden in Prozent'
        #Dynamische Werte füllen
        for i in query_result:
            payment_data.append(float(i.Summe))
            payment_chart_labels.append(i.Titel)

        ## chart no.5 - Stoßzeiten [line-chart] ##
        query = "SELECT WEEKDAY(DATE(cb.creation)) AS Wochentag, COUNT(cb.id) AS Summe FROM cashbox_bill AS cb \
                WHERE creation >= date_sub(current_date(), INTERVAL 7 DAY) AND creation <= current_date() \
                GROUP BY Wochentag \
                ORDER BY Wochentag DESC"

        #Dynamische Werte
        query_result = raw_sql(query)
        peak_times_data = []
        peak_times_chart_labels = []
        #Festwerte
        peak_times_chart_legend = 'Stoßzeiten in Tagen'
        peak_times_chart_x_axes = 'Zeit in Tagen'
        peak_times_chart_y_axes = 'Anzahl der Verkäufe'
        #Dynamische Werte füllen
        for i in query_result:
            if i.Wochentag == 0:
                peak_times_chart_labels.append("Montag")
            elif i.Wochentag == 1:
                peak_times_chart_labels.append("Dienstag")
            elif i.Wochentag == 2:
                peak_times_chart_labels.append("Mittwoch")
            elif i.Wochentag == 3:
                peak_times_chart_labels.append("Donnerstag")
            elif i.Wochentag == 4:
                peak_times_chart_labels.append("Freitag")
            elif i.Wochentag == 5:
                peak_times_chart_labels.append("Samstag")
            elif i.Wochentag == 6:
                peak_times_chart_labels.append("Sonntag")
            peak_times_data.append(i.Summe)

        #
        date_begin = 999
        date_end = 999

        #Context
        context = {
            'form': sales_form,
            'sales_day' : sales_day,
            'sales_week' : sales_week,
            'sales_month' : sales_month,
            'sales_product': sales_product,
            'sales_dienst': sales_dienst,
            'cashbox' : cashbox,
            # chart no.1 - Umsatz Überblick [line-chart] #
            'revenue_products_data' : revenue_products_data,
            'revenue_services_data' : revenue_services_data,
            'revenue_total_data' : revenue_total_data,
            'revenue_chart_x_axes' : revenue_chart_x_axes,
            'revenue_chart_y_axes' : revenue_chart_y_axes,
            'revenue_chart_legend' : revenue_chart_legend,
            'revenue_products_legend' : revenue_products_legend,
            'revenue_services_legend': revenue_services_legend,
            'revenue_total_legend' : revenue_total_legend,
            'date_begin': date_begin,
            'date_end': date_end,
            # chart no.2 - Produkte Überblick (TOP-10 Ranking) [bar-chart]
            'products_chart_labels':products_chart_labels,
            'products_data':products_data,
            'products_chart_x_axes':products_chart_x_axes,
            'products_chart_y_axes':products_chart_y_axes,
            # chart no.3 - Dienstleistungen Überblick (TOP-X Ranking) [bar-chart]
            'services_data' : services_data,
            'services_chart_labels' : services_chart_labels,
            'services_chart_x_axes' : services_chart_x_axes,
            'services_chart_y_axes' : services_chart_y_axes,
            'services_chart_legend' : services_chart_legend,
            ## chart no.4 - Zahlungsmethoden [doughnut-chart] ##
            'payment_data' : payment_data,
            'payment_chart_labels' : payment_chart_labels,
            'payment_chart_legend' : payment_chart_legend,
            ## chart no.5 - Stoßzeiten [line-chart] ##
            'peak_times_data': peak_times_data,
            'peak_times_chart_labels' : peak_times_chart_labels,
            'peak_times_chart_legend' : peak_times_chart_legend,
            'peak_times_chart_x_axes' : peak_times_chart_x_axes
            }
    
    elif request.method == 'POST':
        print("POST")
        sales_form = FormSalesFilter(request.POST)
        #Abfangen des Knopfes und Manipulierung der jeweiligen Daten
        if request.POST.get("mstzfltr"):
            print("Umsatzfilter")
            date = sales_form.data['dateRange']
            print(date)
            date = str(sales_form.data["dateRange"])
            dates = date.split(" - ")
            date_begin = datetime.datetime.strptime(dates[0], '%d.%m.%Y')
            date_end = datetime.datetime.strptime(dates[1], '%d.%m.%Y')
            ## chart no.1 - Umsatz Überblick [line-chart] ##
            #Dynamische Werte
            query = "SELECT WEEKDAY(DATE(creation)) AS Wochentag, SUM(totalcosts) AS Summe, pp.type AS Typ \
                    FROM cashbox_bill AS cb INNER JOIN cashbox_bill_product AS cbp ON cb.id = cbp.bill_id \
                    INNER JOIN product_product AS pp ON cbp.product_id = pp.id \
                    WHERE creation > '" + str(date_begin) + "' \
                    AND creation < '" + str(date_end) + "' \
                    GROUP BY Wochentag, Typ \
                    ORDER BY Wochentag ASC;"
            query_result = raw_sql(query)
            query2 = "SELECT WEEKDAY(DATE(creation)) AS Wochentag, SUM(totalcosts) AS Summe \
                    FROM cashbox_bill AS cb INNER JOIN cashbox_bill_product AS cbp ON cb.id = cbp.bill_id \
                    INNER JOIN product_product AS pp ON cbp.product_id = pp.id \
                    WHERE creation > '" + str(date_begin) + "' \
                    AND creation < '" + str(date_end) + "' \
                    GROUP BY Wochentag \
                    ORDER BY Wochentag ASC;"
            query2_result = raw_sql(query2)
            revenue_products_data = []
            revenue_services_data = []
            revenue_total_data = []
            #Festwerte
            revenue_chart_x_axes = 'Zeit in Tagen'
            revenue_chart_y_axes = 'Umsatz in €'
            revenue_chart_legend = 'Umsatz'
            revenue_products_legend = 'Produkte'
            revenue_services_legend = 'Dienstleistungen'
            revenue_total_legend = 'Gesamt'
            #Dynamische Werte füllen
            for i in query_result:
                if i.Wochentag == 0:
                    tmp = "Montag"
                elif i.Wochentag == 1:
                    tmp = "Dienstag"
                elif i.Wochentag == 2:
                    tmp = "Mittwoch"
                elif i.Wochentag == 3:
                    tmp = "Donnerstag"
                elif i.Wochentag == 4:
                    tmp = "Freitag"
                elif i.Wochentag == 5:
                    tmp = "Samstag"
                elif i.Wochentag ==6:
                    tmp = "Sonntag"

                if i.Typ == "PR":
                    revenue_products_data.append([tmp,float(i.Summe)])
                elif i.Typ == "DI":
                    revenue_services_data.append([tmp,float(i.Summe)])
            
            for i in query2_result:
                if i.Wochentag == 0:
                    revenue_total_data.append(["Montag",float(i.Summe)])
                elif i.Wochentag == 1:
                    revenue_total_data.append(["Dienstag",float(i.Summe)])
                elif i.Wochentag == 2:
                    revenue_total_data.append(["Mittwoch",float(i.Summe)])
                elif i.Wochentag == 3:
                    revenue_total_data.append(["Donnerstag",float(i.Summe)])
                elif i.Wochentag == 4:
                    revenue_total_data.append(["Freitag",float(i.Summe)])
                elif i.Wochentag == 5:
                    revenue_total_data.append(["Samstag",float(i.Summe)])
                elif i.Wochentag == 6:
                    revenue_total_data.append(["Sonntag",float(i.Summe)])


        elif request.POST.get("prdktfltr"):
            print("Produktfilter")
            limit = sales_form.data['radioTOP']
            if limit == '5':
                query = "SELECT product.description AS Produkt, SUM(DISTINCT(amount)) AS Summe \
                FROM product_product AS product INNER JOIN cashbox_bill_product AS products \
                ON product.id = products.product_id  \
                GROUP BY(description) \
                ORDER BY Summe ASC \
                LIMIT 5;"

                #Dynamische Werte
                query_result = raw_sql(query)
                products_chart_labels = []
                products_data = []

                #Festwerte
                products_chart_x_axes = 'Produkte'
                products_chart_y_axes = 'Anzahl der Verkäufe pro Produkt'

                #Dynamische Werte füllen
                for i in query_result:
                    products_chart_labels.append(i.Produkt)
                    products_data.append(i.Summe)
        
            elif limit == '10':
                query = "SELECT product.description AS Produkt, SUM(DISTINCT(amount)) AS Summe \
                FROM product_product AS product INNER JOIN cashbox_bill_product AS products \
                ON product.id = products.product_id  \
                GROUP BY(description) \
                ORDER BY Summe ASC \
                LIMIT 10;"

                #Dynamische Werte
                query_result = raw_sql(query)
                products_chart_labels = []
                products_data = []

                #Festwerte
                products_chart_x_axes = 'Produkte'
                products_chart_y_axes = 'Anzahl der Verkäufe pro Produkt'

                #Dynamische Werte füllen
                for i in query_result:
                    products_chart_labels.append(i.Produkt)
                    products_data.append(i.Summe)
        

        elif request.POST.get("dnstlstngsfltr"):
            print("Dienstleistungsfilter")
            limit = sales_form.data['radioTOP']
            if limit == '5':
                ## chart no.3 - Dienstleistungen Überblick (TOP-X Ranking) [bar-chart] ##
                query = "SELECT pc.title AS Kategorie, SUM(cbp.amount) AS Summe \
                        FROM product_category AS pc \
                        INNER JOIN product_product_category AS ppc ON pc.id = ppc.category_id \
                        INNER JOIN product_product AS pp ON ppc.product_id = pp.id \
                        INNER JOIN cashbox_bill_product AS cbp ON pp.id = cbp.product_id \
                        GROUP BY (pc.title) \
                        ORDER BY Summe DESC \
                        LIMIT 5;"          
                #Dynamische Werte
                query_result = raw_sql(query)
                services_data = []
                services_chart_labels = []
                #Festwerte
                services_chart_x_axes = 'Kategoriename'
                services_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'
                services_chart_legend = 'TOP 5 Dienstleistungen'
                #Dynamische Werte füllen
                for i in query_result:
                    services_data.append(i.Summe)
                    services_chart_labels.append(i.Kategorie)
        
            elif limit == '10':
                ## chart no.3 - Dienstleistungen Überblick (TOP-X Ranking) [bar-chart] ##
                query = "SELECT pc.title AS Kategorie, SUM(cbp.amount) AS Summe \
                        FROM product_category AS pc \
                        INNER JOIN product_product_category AS ppc ON pc.id = ppc.category_id \
                        INNER JOIN product_product AS pp ON ppc.product_id = pp.id \
                        INNER JOIN cashbox_bill_product AS cbp ON pp.id = cbp.product_id \
                        GROUP BY (pc.title) \
                        ORDER BY Summe DESC \
                        LIMIT 10;"          
                #Dynamische Werte
                query_result = raw_sql(query)
                services_data = []
                services_chart_labels = []
                #Festwerte
                services_chart_x_axes = 'Kategoriename'
                services_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'
                services_chart_legend = 'TOP 5 Dienstleistungen'
                #Dynamische Werte füllen
                for i in query_result:
                    services_data.append(i.Summe)
                    services_chart_labels.append(i.Kategorie)

        elif request.POST.get("stßztnfltr"):
            print("Stoßzeitenfilter")
            typ = sales_form.data["radioDAY"]
            if typ == "day":
                ## chart no.5 - Stoßzeiten [line-chart] ##
                query = "SELECT WEEKDAY(DATE(cb.creation)) AS Wochentag, COUNT(cb.id) AS Summe FROM cashbox_bill AS cb \
                        WHERE creation >= date_sub(current_date(), INTERVAL 7 DAY) AND creation <= current_date() \
                        GROUP BY Wochentag \
                        ORDER BY Wochentag DESC"

                #Dynamische Werte
                query_result = raw_sql(query)
                peak_times_data = []
                peak_times_chart_labels = []
                #Festwerte
                peak_times_chart_legend = 'Stoßzeiten in Tagen'
                peak_times_chart_x_axes = 'Zeit in Tagen'
                peak_times_chart_y_axes = 'Anzahl der Verkäufe'
                #Dynamische Werte füllen
                for i in query_result:
                    if i.Wochentag == 0:
                        peak_times_chart_labels.append("Montag")
                    elif i.Wochentag == 1:
                        peak_times_chart_labels.append("Dienstag")
                    elif i.Wochentag == 2:
                        peak_times_chart_labels.append("Mittwoch")
                    elif i.Wochentag == 3:
                        peak_times_chart_labels.append("Donnerstag")
                    elif i.Wochentag == 4:
                        peak_times_chart_labels.append("Freitag")
                    elif i.Wochentag == 5:
                        peak_times_chart_labels.append("Samstag")
                    elif i.Wochentag == 6:
                        peak_times_chart_labels.append("Sonntag")
                    peak_times_data.append(i.Summe)
            elif typ == "hours":
                print("hours")
                target_day = (int(sales_form.data["day"]) -1)
                sub = 0 #Vor wievielen Tagen fand der target_day statt?
                date = datetime.today()
                date_day = date.weekday()
        
                while str(date_day) != str(target_day):
                    sub+=1
                    date = datetime.today() - timedelta(days=sub)
                    date_day = date.weekday()
            
                ## chart no.5 - Stoßzeiten [line-chart] ##
                query = "SELECT TIME(DATE_FORMAT(creation, '%Y-%m-%d %H:00:00')) AS Time, \
                        COUNT(cb.id) AS Summe \
                        FROM cashbox_bill AS cb \
                        WHERE DATE(creation) = DATE_SUB(CURDATE(), INTERVAL " + str(sub) + " DAY) \
                        GROUP BY Time ASC"

                #Dynamische Werte
                query_result = raw_sql(query)
                peak_times_data = []
                peak_times_chart_labels = []
                #Festwerte
                peak_times_chart_legend = 'Stoßzeiten in Stunden'
                peak_times_chart_x_axes = 'Zeit in Stunden'
                peak_times_chart_y_axes = 'Anzahl der Verkäufe'
                #Dynamische Werte füllen
                for i in query_result:
                    peak_times_data.append(i.Summe)
                    peak_times_chart_labels.append(i.Time)

        print(date_begin.day)
        print(date_end.day)

        ##
        #Context
        context = {
            'form': sales_form,
            'sales_day' : sales_day,
            'sales_week' : sales_week,
            'sales_month' : sales_month,
            'sales_product': sales_product,
            'sales_dienst': sales_dienst,
            'cashbox' : cashbox,
            # chart no.1 - Umsatz Überblick [line-chart] #
            'revenue_products_data' : revenue_products_data,
            'revenue_services_data' : revenue_services_data,
            'revenue_total_data' : revenue_total_data,
            'revenue_chart_x_axes' : revenue_chart_x_axes,
            'revenue_chart_y_axes' : revenue_chart_y_axes,
            'revenue_chart_legend' : revenue_chart_legend,
            'revenue_products_legend' : revenue_products_legend,
            'revenue_services_legend': revenue_services_legend,
            'revenue_total_legend' : revenue_total_legend,
            'date_begin': date_begin.day,
            'date_end': date_end.day,
            # chart no.2 - Produkte Überblick (TOP-10 Ranking) [bar-chart]
            'products_chart_labels':products_chart_labels,
            'products_data':products_data,
            'products_chart_x_axes':products_chart_x_axes,
            'products_chart_y_axes':products_chart_y_axes,
            # chart no.3 - Dienstleistungen Überblick (TOP-X Ranking) [bar-chart]
            'services_data' : services_data,
            'services_chart_labels' : services_chart_labels,
            'services_chart_x_axes' : services_chart_x_axes,
            'services_chart_y_axes' : services_chart_y_axes,
            'services_chart_legend' : services_chart_legend,
            ## chart no.4 - Zahlungsmethoden [doughnut-chart] ##
            'payment_data' : payment_data,
            'payment_chart_labels' : payment_chart_labels,
            'payment_chart_legend' : payment_chart_legend,
            ## chart no.5 - Stoßzeiten [line-chart] ##
            'peak_times_data': peak_times_data,
            'peak_times_chart_labels' : peak_times_chart_labels,
            'peak_times_chart_legend' : peak_times_chart_legend,
            'peak_times_chart_x_axes' : peak_times_chart_x_axes
            }


    return render(request, 'analyzation_sales.html', context)

# CustomerView
def analyzation_customers_view(request, *args, **kwargs):
    global peak_times_data, peak_times_chart_labels, peak_times_chart_legend, peak_times_chart_x_axes, peak_times_chart_y_axes, payment_data, payment_chart_labels
    global payment_chart_legend, products_chart_labels, products_data, products_chart_x_axes, products_chart_y_axes, services_chart_legend, services_data, services_chart_labels
    global services_chart_x_axes, services_chart_y_axes, services_chart_legend
    context = {}
    if request.method == 'GET':
        customerForm = FormCustomerFilter()
        # Standarddaten
        ## chart no.1 - Stoßzeiten [line-chart] ##
        query = "SELECT WEEKDAY(DATE(cb.creation)) AS Wochentag, COUNT(cb.id) AS Summe FROM cashbox_bill AS cb \
                WHERE creation >= date_sub(current_date(), INTERVAL 7 DAY) AND creation <= current_date() \
                GROUP BY Wochentag \
                ORDER BY Wochentag DESC"
        #Dynamische Werte
        query_result = raw_sql(query)
        peak_times_data = []
        peak_times_chart_labels = []
        #Festwerte
        peak_times_chart_legend = 'Stoßzeiten in Tagen'
        peak_times_chart_x_axes = 'Zeit in Tagen'
        peak_times_chart_y_axes = 'Anzahl der Verkäufe'
        #Dynamische Werte füllen
        for i in query_result:
            if i.Wochentag == 0:
                peak_times_chart_labels.append("Montag")
            elif i.Wochentag == 1:
                peak_times_chart_labels.append("Dienstag")
            elif i.Wochentag == 2:
                peak_times_chart_labels.append("Mittwoch")
            elif i.Wochentag == 3:
                peak_times_chart_labels.append("Donnerstag")
            elif i.Wochentag == 4:
                peak_times_chart_labels.append("Freitag")
            elif i.Wochentag == 5:
                peak_times_chart_labels.append("Samstag")
            elif i.Wochentag == 6:
                peak_times_chart_labels.append("Sonntag")
            peak_times_data.append(i.Summe)

        ## chart no.3 - Zahlungsmethoden [doughnut-chart] ##
        query = "SELECT cp.title AS Titel, (ROUND(COUNT(cp.id) / (SELECT COUNT(*) AS ges FROM cashbox_bill), 2) * 100) AS Summe \
                FROM cashbox_bill AS cb \
                INNER JOIN cashbox_paymenttool AS cp ON cb.paymenttool_id = cp.id \
                GROUP BY cp.title \
                LIMIT 5;"
        #Dynamische Werte
        query_result = raw_sql(query)
        payment_data = []
        payment_chart_labels = []
        #Festwerte
        payment_chart_legend = 'Zahlungsmethoden in Prozent'
        #Dynamische Werte füllen
        for i in query_result:
            payment_data.append(i.Summe)
            payment_chart_labels.append(i.Titel)
        
         ## chart no.6 - Produkte Überblick (TOP-X Ranking => generell) [bar-chart] ##
        query = "SELECT product.description AS Produkt, SUM(DISTINCT(amount)) AS Summe \
                FROM product_product AS product INNER JOIN cashbox_bill_product AS products \
                ON product.id = products.product_id  \
                GROUP BY(description) \
                ORDER BY Summe ASC \
                LIMIT 5;"

        #Dynamische Werte
        query_result = raw_sql(query)
        products_chart_labels = []
        products_data = []

        #Festwerte
        products_chart_x_axes = 'Produkte'
        products_chart_y_axes = 'Anzahl der Verkäufe pro Produkt'

        #Dynamische Werte füllen
        for i in query_result:
            products_chart_labels.append(i.Produkt)
            products_data.append(i.Summe)
        
        ## chart no.8 - Dienstleistungen Überblick (TOP-X Ranking => generell) [bar-chart] ##
        query = "SELECT pc.title AS Kategorie, SUM(cbp.amount) AS Summe \
                FROM product_category AS pc \
                INNER JOIN product_product_category AS ppc ON pc.id = ppc.category_id \
                INNER JOIN product_product AS pp ON ppc.product_id = pp.id \
                INNER JOIN cashbox_bill_product AS cbp ON pp.id = cbp.product_id \
                GROUP BY (pc.title) \
                ORDER BY Summe DESC \
                LIMIT 5;"          
        #Dynamische Werte
        query_result = raw_sql(query)
        services_data = []
        services_chart_labels = []
        #Festwerte
        services_chart_x_axes = 'Kategoriename'
        services_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'
        services_chart_legend = 'TOP 5 Dienstleistungen'
        #Dynamische Werte füllen
        for i in query_result:
            services_data.append(i.Summe)
            services_chart_labels.append(i.Kategorie)
            
        #context
        context = {'form': customerForm,
                   # chart no.1 - Stoßzeiten [line-chart]
                   'peak_times_data' : peak_times_data,
                   'peak_times_chart_labels' : peak_times_chart_labels,
                   'peak_times_chart_legend' : peak_times_chart_legend,
                   'peak_times_chart_x_axes' : peak_times_chart_x_axes,
                   'peak_times_chart_y_axes' : peak_times_chart_y_axes,
                   # chart no.3 - Zahlungsmethoden [doughnut-chart] #
                   'payment_data' : payment_data,
                   'payment_chart_labels' : payment_chart_labels,
                   'payment_chart_legend' : payment_chart_legend,
                   # chart no.6 - Produkte Überblick (TOP-X Ranking => generell) [bar-chart]
                   'products_chart_labels' : products_chart_labels,
                   'products_data' : products_data,
                   'products_chart_x_axes' : products_chart_x_axes,
                   'products_chart_y_axes' : products_chart_y_axes,
                   'services_chart_legend' : services_chart_legend,
                   # chart no.8 - Dienstleistungen Überblick 
                   'services_data' : services_data,
                   'services_chart_labels' : services_chart_labels,
                   'services_chart_x_axes' : services_chart_x_axes,
                   'services_chart_y_axes' : services_chart_y_axes,
                   'services_chart_legend' : services_chart_legend

                  }
    
    elif request.method == 'POST':
        customerForm = FormCustomerFilter(request.POST)
        
        if request.POST.get("stßztnfltr"):
            print("Stoßzeitenfilter")
            typ = customerForm.data["radioDAY"]
            if typ == "day":
                ## chart no.5 - Stoßzeiten [line-chart] ##
                query = "SELECT WEEKDAY(DATE(cb.creation)) AS Wochentag, COUNT(cb.id) AS Summe FROM cashbox_bill AS cb \
                        WHERE creation >= date_sub(current_date(), INTERVAL 7 DAY) AND creation <= current_date() \
                        GROUP BY Wochentag \
                        ORDER BY Wochentag DESC"

                #Dynamische Werte
                query_result = raw_sql(query)
                peak_times_data = []
                peak_times_chart_labels = []
                #Festwerte
                peak_times_chart_legend = 'Stoßzeiten in Tagen'
                peak_times_chart_x_axes = 'Zeit in Tagen'
                peak_times_chart_y_axes = 'Anzahl der Verkäufe'
                #Dynamische Werte füllen
                for i in query_result:
                    if i.Wochentag == 0:
                        peak_times_chart_labels.append("Montag")
                    elif i.Wochentag == 1:
                        peak_times_chart_labels.append("Dienstag")
                    elif i.Wochentag == 2:
                        peak_times_chart_labels.append("Mittwoch")
                    elif i.Wochentag == 3:
                        peak_times_chart_labels.append("Donnerstag")
                    elif i.Wochentag == 4:
                        peak_times_chart_labels.append("Freitag")
                    elif i.Wochentag == 5:
                        peak_times_chart_labels.append("Samstag")
                    elif i.Wochentag == 6:
                        peak_times_chart_labels.append("Sonntag")
                    peak_times_data.append(i.Summe)
            
            elif typ == "hours":
                print("hours")
                target_day = (int(customerForm.data["day"]) -1)
                sub = 0 #Vor wievielen Tagen fand der target_day statt?
                date = datetime.today()
                date_day = date.weekday()
        
                while str(date_day) != str(target_day):
                    sub+=1
                    date = datetime.today() - timedelta(days=sub)
                    date_day = date.weekday()
            
                ## chart no.5 - Stoßzeiten [line-chart] ##
                query = "SELECT TIME(DATE_FORMAT(creation, '%Y-%m-%d %H:00:00')) AS Time, \
                        COUNT(cb.id) AS Summe \
                        FROM cashbox_bill AS cb \
                        WHERE DATE(creation) = DATE_SUB(CURDATE(), INTERVAL " + str(sub) + " DAY) \
                        GROUP BY Time ASC"

                #Dynamische Werte
                query_result = raw_sql(query)
                peak_times_data = []
                peak_times_chart_labels = []
                #Festwerte
                peak_times_chart_legend = 'Stoßzeiten in Stunden'
                peak_times_chart_x_axes = 'Zeit in Stunden'
                peak_times_chart_y_axes = 'Anzahl der Verkäufe'
                #Dynamische Werte füllen
                for i in query_result:
                    peak_times_data.append(i.Summe)
                    peak_times_chart_labels.append(i.Time)
            
        elif request.POST.get("prdktfltr"):
            print("Produktfilter")
            limit = customerForm.data["radioTOP"]
            if limit == "5":
                query = "SELECT product.description AS Produkt, SUM(DISTINCT(amount)) AS Summe \
                FROM product_product AS product INNER JOIN cashbox_bill_product AS products \
                ON product.id = products.product_id  \
                GROUP BY(description) \
                ORDER BY Summe ASC \
                LIMIT 5;"

                #Dynamische Werte
                query_result = raw_sql(query)
                products_chart_labels = []
                products_data = []

                #Festwerte
                products_chart_x_axes = 'Produkte'
                products_chart_y_axes = 'Anzahl der Verkäufe pro Produkt'

                #Dynamische Werte füllen
                for i in query_result:
                    products_chart_labels.append(i.Produkt)
                    products_data.append(i.Summe)
            elif limit == "10":
                query = "SELECT product.description AS Produkt, SUM(DISTINCT(amount)) AS Summe \
                FROM product_product AS product INNER JOIN cashbox_bill_product AS products \
                ON product.id = products.product_id  \
                GROUP BY(description) \
                ORDER BY Summe ASC \
                LIMIT 10;"

                #Dynamische Werte
                query_result = raw_sql(query)
                products_chart_labels = []
                products_data = []

                #Festwerte
                products_chart_x_axes = 'Produkte'
                products_chart_y_axes = 'Anzahl der Verkäufe pro Produkt'

                #Dynamische Werte füllen
                for i in query_result:
                    products_chart_labels.append(i.Produkt)
                    products_data.append(i.Summe)
        

        elif request.POST.get("dnstlstngfltr"):
            print("Dienstleistungsfilter")
            limit = customerForm.data["radioTOP"]
            if limit == "5":
                ## chart no.3 - Dienstleistungen Überblick (TOP-5 Ranking) [bar-chart] ##
                query = "SELECT pc.title AS Kategorie, SUM(cbp.amount) AS Summe \
                        FROM product_category AS pc \
                        INNER JOIN product_product_category AS ppc ON pc.id = ppc.category_id \
                        INNER JOIN product_product AS pp ON ppc.product_id = pp.id \
                        INNER JOIN cashbox_bill_product AS cbp ON pp.id = cbp.product_id \
                        GROUP BY (pc.title) \
                        ORDER BY Summe DESC \
                        LIMIT 5;"          
                #Dynamische Werte
                query_result = raw_sql(query)
                services_data = []
                services_chart_labels = []
                #Festwerte
                services_chart_x_axes = 'Kategoriename'
                services_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'
                services_chart_legend = 'TOP 5 Dienstleistungen'
                #Dynamische Werte füllen
                for i in query_result:
                    services_data.append(i.Summe)
                    services_chart_labels.append(i.Kategorie)
        
            elif limit == "10":
                ## chart no.3 - Dienstleistungen Überblick (TOP-10 Ranking) [bar-chart] ##
                query = "SELECT pc.title AS Kategorie, SUM(cbp.amount) AS Summe \
                        FROM product_category AS pc \
                        INNER JOIN product_product_category AS ppc ON pc.id = ppc.category_id \
                        INNER JOIN product_product AS pp ON ppc.product_id = pp.id \
                        INNER JOIN cashbox_bill_product AS cbp ON pp.id = cbp.product_id \
                        GROUP BY (pc.title) \
                        ORDER BY Summe DESC \
                        LIMIT 10;"          
                #Dynamische Werte
                query_result = raw_sql(query)
                services_data = []
                services_chart_labels = []
                #Festwerte
                services_chart_x_axes = 'Kategoriename'
                services_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'
                services_chart_legend = 'TOP 5 Dienstleistungen'
                #Dynamische Werte füllen
                for i in query_result:
                    services_data.append(i.Summe)
                    services_chart_labels.append(i.Kategorie)

        # Context
        context = {'form': customerForm,
                   # chart no.1 - Stoßzeiten [line-chart]
                   'peak_times_data' : peak_times_data,
                   'peak_times_chart_labels' : peak_times_chart_labels,
                   'peak_times_chart_legend' : peak_times_chart_legend,
                   'peak_times_chart_x_axes' : peak_times_chart_x_axes,
                   'peak_times_chart_y_axes' : peak_times_chart_y_axes,
                   # chart no.3 - Zahlungsmethoden [doughnut-chart] #
                   'payment_data' : payment_data,
                   'payment_chart_labels' : payment_chart_labels,
                   'payment_chart_legend' : payment_chart_legend,
                   # chart no.6 - Produkte Überblick (TOP-X Ranking => generell) [bar-chart]
                   'products_chart_labels' : products_chart_labels,
                   'products_data' : products_data,
                   'products_chart_x_axes' : products_chart_x_axes,
                   'products_chart_y_axes' : products_chart_y_axes,
                   'services_chart_legend' : services_chart_legend,
                   # chart no.8 - Dienstleistungen Überblick 
                   'services_data' : services_data,
                   'services_chart_labels' : services_chart_labels,
                   'services_chart_x_axes' : services_chart_x_axes,
                   'services_chart_y_axes' : services_chart_y_axes,
                   'services_chart_legend' : services_chart_legend

                  }

    return render(request, 'analyzation_customers.html', context)

#EmployeesView
def analyzation_employees_view(request, *args, **kwargs):
    global employee_data, employee_times_x_axes, employee_times_y_axes, employee_times_chart_legend, employee_revenue_data, employee_revenue_chart_legend, employee_revenue_x_axes
    global employee_revenue_y_axes
    context = {}
    if request.method == 'GET':
        analystForm = FormEmployeeFilter()
        # Standarddaten
        # chart no.1 - Mitarbeiterzeiten [line-chart]
        # Dynamische Werte
        employee_data = []
        # Festwerte
        employee_times_x_axes = 'Zeit in Tagen'
        employee_times_y_axes = 'Anzahl der Arbeitsstunnden pro Kassierer'
        employee_times_chart_legend = 'Mitarbeiterzeiten'
        # Dynamische Werte Füllen
        query = "SELECT DISTINCT aaa.user_id AS Nutzer, CONCAT(au.first_name, ' ', au.last_name) AS Nutzername \
                FROM authorization_active_accounts AS aaa \
                INNER JOIN auth_user AS au ON aaa.user_id = au.id \
                INNER JOIN analyzation_worktime AS aw ON au.id = aw.employee_id \
                WHERE aw.begin >= DATE_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY) \
                AND aw.end <= CURRENT_TIMESTAMP();"      
        query_aa = raw_sql(query) #Alle Nutzer mit Arbeitszeiten in den letzen 7 Tagen
        count = len(query_aa)

        for x in range(count): #iteration über alle Nutzer
            id = query_aa[x].Nutzer
            query = "SELECT DATE(aw.end) AS Datum, \
                     SEC_TO_TIME(SUM(TIME_TO_SEC(TIMEDIFF(aw.end, aw.begin)))) AS Arbeitszeit \
                     FROM authorization_active_accounts AS aaa \
                     INNER JOIN auth_user AS au ON aaa.user_id = au.id \
                     INNER JOIN analyzation_worktime AS aw ON au.id = aw.employee_id \
                     WHERE aw.end IS NOT NULL \
                     AND aw.employee_id = " + str(id) + " \
                     AND aw.begin >= DATE_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY) \
                     AND aw.end <= CURRENT_TIMESTAMP() \
                     GROUP BY DATE(aw.end) \
                     ORDER BY Datum DESC;"
            user_data = raw_sql(query) #Alle Arbeitszeiten für Nutzer in den letzen 7 Tagen
            sets = len(user_data)
            employee_data.append([query_aa[x].Nutzername])
            for i in range(sets):      #Füllen von Werten
                    employee_data[x].extend([[user_data[i].Datum, user_data[i].Arbeitszeit]])
   
        # Datenstruktur ausgeben
        # for i in employee_data:
        #     print(i)

        # chart no.2 - Mitarbeiterumsatz [line-chart]
        # Dynamische Werte
        employee_revenue_data = []
        # Festwerte
        employee_revenue_chart_legend = 'Mitarbeiterumsatz'
        employee_revenue_x_axes = 'Zeit in Tagen'
        employee_revenue_y_axes = 'Anzahl der Arbeitsstunnden pro Kassierer'
        # Dynamische Werte füllen
        query = "SELECT DISTINCT aaa.user_id AS Nutzer, CONCAT(au.first_name, ' ', au.last_name) AS Nutzername \
                FROM authorization_active_accounts AS aaa \
                INNER JOIN auth_user AS au ON aaa.user_id = au.id \
                INNER JOIN auth_user_groups AS aug ON au.id = aug.user_id \
                INNER JOIN auth_group AS ag ON aug.group_id = ag.id \
                INNER JOIN cashbox_bill AS cb ON au.id = cb.employee_id \
                WHERE ag.id = 2 AND cb.creation >= DATE_SUB(CURRENT_TIMESTAMP(),INTERVAL 7 DAY) \
                AND cb.creation <= CURRENT_TIMESTAMP();"
        query_k = raw_sql(query)
        count = len(query_k)

        for x in range(count):
            id = query_k[x].Nutzer
            query = "SELECT DATE(cb.creation) AS Datum, SUM(cb.totalcosts) AS Summe \
                    FROM cashbox_bill AS cb WHERE cb.employee_id = " + str(id) +" \
                    AND cb.creation >= DATE_SUB(CURRENT_TIMESTAMP(), \
                    INTERVAL 7 DAY) AND cb.creation <= CURRENT_TIMESTAMP() \
                    GROUP BY DATE(cb.creation) \
                    ORDER BY Datum DESC;"
            user_data = raw_sql(query)
            sets = len(user_data)
            employee_revenue_data.append([query_k[x].Nutzername])
            
            for i in range(sets):
                employee_revenue_data[x].extend([[user_data[i].Datum, user_data[i].Summe]])
    
        # Datenstruktur ausgeben
        # for i in employee_revenue_data:
        #     print(i)


        #Context
        context = {'form': analystForm,
                # chart no.1 - Mitarbeiterzeiten [line-chart]
                'employee_data' : employee_data,     #Alle Nutzer Mit ihren Zeiten
                'employee_times_x_axes' : employee_times_x_axes,
                'employee_times_y_axes' : employee_times_y_axes,
                'employee_times_chart_legend' : employee_times_chart_legend,
                # chart no.2 - Mitarbeiterumsatz [line-chart]
                'employee_revenue_data' : employee_revenue_data,
                'employee_revenue_chart_legend' : employee_revenue_chart_legend,
                'employee_revenue_x_axes' : employee_revenue_x_axes,
                'employee_revenue_y_axes' : employee_revenue_y_axes
                }                                  
    
    elif request.method == 'POST':
        analystForm = FormEmployeeFilter(request.POST)

        if request.POST.get("mtrbtr_ztn"):
            print("Mitarbeiter Zeiten")
            date = str(analystForm.data["dateRange1"])
            dates = date.split(" - ")
            date_begin = datetime.datetime.strptime(dates[0], '%d.%m.%Y')
            date_end = datetime.datetime.strptime(dates[1], '%d.%m.%Y')
            # chart no.1 - Mitarbeiterzeiten [line-chart]
            # Dynamische Werte
            employee_data = []
            # Festwerte
            employee_times_x_axes = 'Zeit in Tagen'
            employee_times_y_axes = 'Anzahl der Arbeitsstunnden pro Kassierer'
            employee_times_chart_legend = 'Mitarbeiterzeiten'
            # Dynamische Werte Füllen
            query = "SELECT DISTINCT aaa.user_id AS Nutzer, CONCAT(au.first_name, ' ', au.last_name) AS Nutzername \
                    FROM authorization_active_accounts AS aaa \
                    INNER JOIN auth_user AS au ON aaa.user_id = au.id \
                    INNER JOIN analyzation_worktime AS aw ON au.id = aw.employee_id \
                    WHERE aw.begin >= '" + str(date_begin)  + "' \
                    AND aw.end <= '" + str(date_end) + "';"      
            query_aa = raw_sql(query) #Alle Nutzer mit Arbeitszeiten in den letzen 7 Tagen
            count = len(query_aa)

            for x in range(count): #iteration über alle Nutzer
                id = query_aa[x].Nutzer
                query = "SELECT DATE(aw.end) AS Datum, \
                        SEC_TO_TIME(SUM(TIME_TO_SEC(TIMEDIFF(aw.end, aw.begin)))) AS Arbeitszeit \
                        FROM authorization_active_accounts AS aaa \
                        INNER JOIN auth_user AS au ON aaa.user_id = au.id \
                        INNER JOIN analyzation_worktime AS aw ON au.id = aw.employee_id \
                        WHERE aw.end IS NOT NULL \
                        AND aw.employee_id = " + str(id) + " \
                        AND aw.begin >= '" + str(date_begin)  + "' \
                        AND aw.end <= '" + str(date_end) + "' \
                        GROUP BY DATE(aw.end) \
                        ORDER BY Datum DESC;"
                user_data = raw_sql(query) #Alle Arbeitszeiten für Nutzer in den letzen 7 Tagen
                sets = len(user_data)
                employee_data.append([query_aa[x].Nutzername])
                for i in range(sets):      #Füllen von Werten
                        employee_data[x].extend([[user_data[i].Datum, user_data[i].Arbeitszeit]])

        elif request.POST.get("mtrbtr_mstz"):
            print("Mitarbeiter Umsatz")
            date = analystForm.data["dateRange2"]
            dates = date.split(" - ")
            date_begin = datetime.datetime.strptime(dates[0], '%d.%m.%Y')
            date_end = datetime.datetime.strptime(dates[1], '%d.%m.%Y')
            # chart no.2 - Mitarbeiterumsatz [line-chart]
            # Dynamische Werte
            employee_revenue_data = []
            # Festwerte
            employee_revenue_chart_legend = 'Mitarbeiterumsatz'
            employee_revenue_x_axes = 'Zeit in Tagen'
            employee_revenue_y_axes = 'Anzahl der Arbeitsstunnden pro Kassierer'
            # Dynamische Werte füllen
            query = "SELECT DISTINCT aaa.user_id AS Nutzer, CONCAT(au.first_name, ' ', au.last_name) AS Nutzername \
                    FROM authorization_active_accounts AS aaa \
                    INNER JOIN auth_user AS au ON aaa.user_id = au.id \
                    INNER JOIN auth_user_groups AS aug ON au.id = aug.user_id \
                    INNER JOIN auth_group AS ag ON aug.group_id = ag.id \
                    INNER JOIN cashbox_bill AS cb ON au.id = cb.employee_id \
                    WHERE ag.id = 2 AND cb.creation >= '" + str(date_begin) + "' \
                    AND cb.creation <= '" + str(date_end) + "';"
            query_k = raw_sql(query)
            count = len(query_k)

            for x in range(count):
                id = query_k[x].Nutzer
                query = "SELECT DATE(cb.creation) AS Datum, SUM(cb.totalcosts) AS Summe \
                        FROM cashbox_bill AS cb WHERE cb.employee_id = " + str(id) +" \
                        AND cb.creation >= '" + str(date_begin) + "' \
                        cb.creation <= '" + str(date_end) + "' \
                        GROUP BY DATE(cb.creation) \
                        ORDER BY Datum DESC;"
                user_data = raw_sql(query)
                sets = len(user_data)
                employee_revenue_data.append([query_k[x].Nutzername])
                
                for i in range(sets):
                    employee_revenue_data[x].extend([[user_data[i].Datum, user_data[i].Summe]])
    
    context = {'form': analystForm,
                # chart no.1 - Mitarbeiterzeiten [line-chart]
                'employee_data' : employee_data,     #Alle Nutzer Mit ihren Zeiten
                'employee_times_x_axes' : employee_times_x_axes,
                'employee_times_y_axes' : employee_times_y_axes,
                'employee_times_chart_legend' : employee_times_chart_legend,
                # chart no.2 - Mitarbeiterumsatz [line-chart]
                'employee_revenue_data' : employee_revenue_data,
                'employee_revenue_chart_legend' : employee_revenue_chart_legend,
                'employee_revenue_x_axes' : employee_revenue_x_axes,
                'employee_revenue_y_axes' : employee_revenue_y_axes
                }                           

    return render(request, 'analyzation_employees.html', context)

##############################################################
#new API's
class SalesProductList(APIView):
    
    def get(self, request, format=None):
        # chart no.2 - Produkte Überblick (TOP-10 Ranking) [bar-chart]
        query = "SELECT product.description AS Produkt, SUM(DISTINCT(amount)) AS Summe \
                FROM product_product AS product INNER JOIN cashbox_bill_product AS products \
                ON product.id = products.product_id  \
                GROUP BY(description) \
                ORDER BY Summe ASC \
                LIMIT 10;"

        #Dynamische Werte
        query_result = raw_sql(query)
        products_chart_labels = []
        products_data = []

        #Festwerte
        products_chart_x_axes = 'Produkte'
        products_chart_y_axes = 'Anzahl der Verkäufe pro Produkt'

        #Dynamische Werte füllen
        for i in query_result:
            products_chart_labels.append(i.Produkt)
            products_data.append(i.Summe)
        
        context = {
            'products_chart_labels':products_chart_labels,
            'products_data':products_data,
            'products_chart_x_axes':products_chart_x_axes,
            'products_chart_y_axes':products_chart_y_axes,
        }
        return Response(context)
###############################################################


#####################################################################################################################################
#                                                           old                                                                     #
#####################################################################################################################################
# for chart.js with rest-framework
class DashboardChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # chart no.1 - Umsatz Überblick [line-chart]
        revenue_total_data = [26, 39, 44, 64, 92, 64]
        revenue_total_legend = 'Gesamt'
        revenue_products_data = [13, 23, 24, 38, 49, 33]
        revenue_products_legend = 'Produkte'
        revenue_services_data = [13, 16, 20, 26, 43, 31]
        revenue_services_legend = 'Dienstleistungen'
        revenue_chart_legend = 'Umsatz'
        revenue_chart_labels = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag']
        revenue_chart_x_axes = 'Zeit in Tagen'
        revenue_chart_y_axes = 'Umsatz in €'

        #chart no.2 - Produkte Überblick (TOP-X Ranking) [bar-chart]
        products_data = [13, 23, 24, 38, 49, 33]
        products_chart_legend = 'TOP 5 Produkte'
        products_chart_labels = ['Schampoo', 'Spülung', 'Festiger', 'Kamm', 'Bürste']
        products_chart_x_axes = 'Kategoriename'
        products_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'

        #chart no.3 - Dienstleistungen Überblick (TOP-X Ranking) [bar-chart]
        services_data = [13, 16, 20, 26, 43, 31]
        services_chart_legend = 'TOP 5 Dienstleistungen'
        services_chart_labels = ['Damen', 'Colorationen', 'Herren', 'Specials', 'Kinder']
        services_chart_x_axes = 'Kategoriename'
        services_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'

        data = {
            'revenue_total_data': revenue_total_data,
            'revenue_total_legend': revenue_total_legend,
            'revenue_products_data': revenue_products_data,
            'revenue_products_legend': revenue_products_legend,
            'revenue_services_data': revenue_services_data,
            'revenue_services_legend': revenue_services_legend,
            'revenue_chart_legend': revenue_chart_legend,
            'revenue_chart_labels': revenue_chart_labels,
            'revenue_chart_x_axes': revenue_chart_x_axes,
            'revenue_chart_y_axes': revenue_chart_y_axes,
            'products_data': products_data,
            'products_chart_legend': products_chart_legend,
            'products_chart_labels': products_chart_labels,
            'products_chart_x_axes': products_chart_x_axes,
            'products_chart_y_axes': products_chart_y_axes,
            'services_data': services_data,
            'services_chart_legend': services_chart_legend,
            'services_chart_labels': services_chart_labels,
            'services_chart_x_axes': services_chart_x_axes,
            'services_chart_y_axes': services_chart_y_axes
        }
        return Response(data)

# # for chart.js with rest-framework
class SalesChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # chart no.1 - Umsatz Überblick [line-chart]
        revenue_total_data = [26, 39, 44, 64, 92, 64]
        revenue_total_legend = 'Gesamt'
        revenue_products_data = [13, 23, 24, 38, 49, 33]
        revenue_products_legend = 'Produkte'
        revenue_services_data = [13, 16, 20, 26, 43, 31]
        revenue_services_legend = 'Dienstleistungen'
        revenue_chart_legend = 'Umsatz'
        revenue_chart_labels = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag']
        revenue_chart_x_axes = 'Zeit in Tagen'
        revenue_chart_y_axes = 'Umsatz in €'

        # chart no.2 - Produkte Überblick (TOP-X Ranking) [bar-chart]
        products_data = [13, 23, 24, 38, 49, 33]
        products_chart_legend = 'TOP 5 Produkte'
        products_chart_labels = ['Schampoo', 'Spülung', 'Festiger', 'Kamm', 'Bürste']
        products_chart_x_axes = 'Kategoriename'
        products_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'

        # chart no.3 - Dienstleistungen Überblick (TOP-X Ranking) [bar-chart]
        services_data = [13, 16, 20, 26, 43, 31]
        services_chart_legend = 'TOP 5 Dienstleistungen'
        services_chart_labels = ['Damen', 'Colorationen', 'Herren', 'Specials', 'Kinder']
        services_chart_x_axes = 'Kategoriename'
        services_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'

        # chart no.4 - Zahlungsmethoden [doughnut-chart]
        payment_data = [60, 35, 5]
        payment_chart_labels = ['Barzahlung', 'Kartenzahlung', 'ApplePay']
        payment_chart_legend = 'Zahlungsmethoden in Prozent'

        # chart no.5 - Stoßzeiten [line-chart]
        peak_times_data = [13, 16, 20, 26, 43, 31, 0]
        peak_times_chart_labels = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
        peak_times_chart_legend = 'Stoßzeiten in Tagen'
        peak_times_chart_x_axes = 'Zeit in Tagen'
        peak_times_chart_y_axes = 'Anzahl der Kunden'

        data = {
            'revenue_total_data': revenue_total_data,
            'revenue_total_legend': revenue_total_legend,
            'revenue_products_data': revenue_products_data,
            'revenue_products_legend': revenue_products_legend,
            'revenue_services_data': revenue_services_data,
            'revenue_services_legend': revenue_services_legend,
            'revenue_chart_legend': revenue_chart_legend,
            'revenue_chart_labels': revenue_chart_labels,
            'revenue_chart_x_axes': revenue_chart_x_axes,
            'revenue_chart_y_axes': revenue_chart_y_axes,
            'products_data': products_data,
            'products_chart_legend': products_chart_legend,
            'products_chart_labels': products_chart_labels,
            'products_chart_x_axes': products_chart_x_axes,
            'products_chart_y_axes': products_chart_y_axes,
            'services_data': services_data,
            'services_chart_legend': services_chart_legend,
            'services_chart_labels': services_chart_labels,
            'services_chart_x_axes': services_chart_x_axes,
            'services_chart_y_axes': services_chart_y_axes,
            'payment_data': payment_data,
            'payment_chart_labels': payment_chart_labels,
            'payment_chart_legend': payment_chart_legend,
            'peak_times_data': peak_times_data,
            'peak_times_chart_labels': peak_times_chart_labels,
            'peak_times_chart_legend': peak_times_chart_legend,
            'peak_times_chart_x_axes': peak_times_chart_x_axes,
            'peak_times_chart_y_axes': peak_times_chart_y_axes
        }
        return Response(data)

# # for chart.js with rest-framework
class CustomerChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # chart no.1 - Stoßzeiten [line-chart]
        peak_times_data = [13, 16, 20, 26, 43, 31, 0]
        peak_times_chart_labels = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
        peak_times_chart_legend = 'Stoßzeiten in Tagen'
        peak_times_chart_x_axes = 'Zeit in Tagen'
        peak_times_chart_y_axes = 'Anzahl der Kunden'

        # chart no.2 - Kundenart [doughnut-chart]
        customers_data = [60, 40]
        customers_chart_labels = ['Stammkunden', 'Neukunden']
        customers_chart_legend = 'Kundenart in Prozent'

        # chart no.3 - Zahlungsmethode [doughnut-chart]
        payment_data = [[60], [35], [5]]
        payment_chart_labels = ['Barzahlung', 'Kartenzahlung', 'ApplePay']
        payment_chart_legend = 'Zahlungsmethoden in Prozent'

        # chart no.4 - Gefunden durch [doughnut-chart]
        found_through_data = [40, 25, 20, 15]
        found_through_chart_labels = ['Zufall', 'Soziale Medien', 'Flyer', 'Webseite']
        found_through_chart_legend = 'Kundenart in Prozent'

        # chart no.5 - Bewertung in Sternen [doughnut-chart]
        rating_data = [60, 20, 15, 5, 0, 0]
        rating_chart_labels = ['5 Sterne', '4 Sterne', '3 Sterne', '2 Sterne', '1 Sterne', '0 Sterne']
        rating_chart_legend = 'Zahlungsmethoden in Prozent'

        # chart no.6 - Produkte Überblick (TOP-X Ranking => generell) [bar-chart]
        products_1_data = [13, 23, 24, 38, 49, 33]
        products_1_chart_legend = 'TOP 5 Produkte (Gesamt)'
        products_1_chart_labels = ['Schampoo', 'Spülung', 'Festiger', 'Kamm', 'Bürste']
        products_1_chart_x_axes = 'Kategoriename'
        products_1_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'

        # chart no.7 - Produkte Überblick (TOP-X Ranking => nach Stammkunden) [bar-chart]
        products_2_data = [13, 23, 24, 38, 49, 33]
        products_2_chart_legend = 'TOP 5 Produkte (nach Stammkunden)'
        products_2_chart_labels = ['Schampoo', 'Spülung', 'Festiger', 'Kamm', 'Bürste']
        products_2_chart_x_axes = 'Kategoriename'
        products_2_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'

        # chart no.8 - Dienstleistungen Überblick (TOP-X Ranking => generell) [bar-chart]
        services_1_data = [13, 16, 20, 26, 43, 31]
        services_1_chart_legend = 'TOP 5 Dienstleistungen (Gesamt)'
        services_1_chart_labels = ['Damen', 'Colorationen', 'Herren', 'Specials', 'Kinder']
        services_1_chart_x_axes = 'Kategoriename'
        services_1_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'

        # chart no.9 - Dienstleistungen Überblick (TOP-X Ranking => nach Stammkunden) [bar-chart]
        services_2_data = [13, 16, 20, 26, 43, 31]
        services_2_chart_legend = 'TOP 5 Dienstleistungen (nach Stammkunden)'
        services_2_chart_labels = ['Damen', 'Colorationen', 'Herren', 'Specials', 'Kinder']
        services_2_chart_x_axes = 'Kategoriename'
        services_2_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'

        data = {
            'peak_times_data': peak_times_data,
            'peak_times_chart_labels': peak_times_chart_labels,
            'peak_times_chart_legend': peak_times_chart_legend,
            'peak_times_chart_x_axes': peak_times_chart_x_axes,
            'peak_times_chart_y_axes': peak_times_chart_y_axes,
            'customers_data': customers_data,
            'customers_chart_labels': customers_chart_labels,
            'customers_chart_legend': customers_chart_legend,
            'payment_data': payment_data,
            'payment_chart_labels': payment_chart_labels,
            'payment_chart_legend': payment_chart_legend,
            'found_through_data': found_through_data,
            'found_through_chart_labels': found_through_chart_labels,
            'found_through_chart_legend': found_through_chart_legend,
            'rating_data': rating_data,
            'rating_chart_labels': rating_chart_labels,
            'rating_chart_legend': rating_chart_legend,
            'products_1_data': products_1_data,
            'products_1_chart_legend': products_1_chart_legend,
            'products_1_chart_labels': products_1_chart_labels,
            'products_1_chart_x_axes': products_1_chart_x_axes,
            'products_1_chart_y_axes': products_1_chart_y_axes,
            'products_2_data': products_2_data,
            'products_2_chart_legend': products_2_chart_legend,
            'products_2_chart_labels': products_2_chart_labels,
            'products_2_chart_x_axes': products_2_chart_x_axes,
            'products_2_chart_y_axes': products_2_chart_y_axes,
            'services_1_data': services_1_data,
            'services_1_chart_legend': services_1_chart_legend,
            'services_1_chart_labels': services_1_chart_labels,
            'services_1_chart_x_axes': services_1_chart_x_axes,
            'services_1_chart_y_axes': services_1_chart_y_axes,
            'services_2_data': services_2_data,
            'services_2_chart_legend': services_2_chart_legend,
            'services_2_chart_labels': services_2_chart_labels,
            'services_2_chart_x_axes': services_2_chart_x_axes,
            'services_2_chart_y_axes': services_2_chart_y_axes
        }
        return Response(data)

# # for chart.js with rest-framework
class EmployeeChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # chart no.1 - Mitarbeiterzeiten [line-chart]
        employee_times_data = [[0, 4, 4, 4, 4, 8, 8], [8, 8, 8, 8, 0, 0, 0], [2, 2, 2, 2, 0, 0, 8]]
        employee_times_labels = ['Mitarbeitername 1', 'Mitarbeitername 2', 'Mitarbeitername 3']
        employee_times_chart_labels = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
        
        employee_times_chart_legend = 'Mitarbeiterzeiten'
        employee_times_x_axes = 'Zeit in Tagen'
        employee_times_y_axes = 'Anzahl der Arbeitsstunnden pro Kassierer'

        # chart no.2 - Mitarbeiterumsatz [line-chart]
        employee_revenue_data = [[0, 4, 4, 4, 4, 8, 8], [8, 8, 8, 8, 0, 0, 0], [2, 2, 2, 2, 0, 0, 8]]
        employee_revenue_labels = ['Mitarbeitername 1', 'Mitarbeitername 2', 'Mitarbeitername 3']
        employee_revenue_chart_labels = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag',
                                         'Sonntag']
        employee_revenue_chart_legend = 'Mitarbeiterumsatz'
        employee_revenue_x_axes = 'Zeit in Tagen'
        employee_revenue_y_axes = 'Anzahl der Arbeitsstunnden pro Kassierer'

        data = {
            'employee_times_data': employee_times_data,
            'employee_times_labels': employee_times_labels,
            'employee_times_chart_labels': employee_times_chart_labels,
            'employee_times_chart_legend': employee_times_chart_legend,
            'employee_times_x_axes': employee_times_x_axes,
            'employee_times_y_axes': employee_times_y_axes,
            'employee_revenue_data': employee_revenue_data,
            'employee_revenue_labels': employee_revenue_labels,
            'employee_revenue_chart_labels': employee_revenue_chart_labels,
            'employee_revenue_chart_legend': employee_revenue_chart_legend,
            'employee_revenue_x_axes': employee_revenue_x_axes,
            'employee_revenue_y_axes': employee_revenue_y_axes
        }
        return Response(data)
##############################################################################################################################

# ----------------------------------------------------------------------------------------------------------------------
# class DashboardView(View):
#    def get(self, request, *args, **kwargs):
#        return render(request, 'analyzation_dashboard.html', {'customers': 10})


# def get_data(request, *args, **kwargs):
#    data = {
#        'sales': 100,
#        'customers': 10,
#    }
#    return JsonResponse(data) # http response
