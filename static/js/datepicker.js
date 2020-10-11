let startDate = '';
let endDate = '';

$(function(){
    let dateRangePicker = document.getElementById('dateRangePicker');
        let pickerRange = new Lightpick({
        field: dateRangePicker,
        singleDate: false,
        lang: 'de',
        format: 'DD.MM.YYYY',
        disableWeekends: false,
        minDays: 6,
        maxDays: 6,
        weekdayStyle: 'long',
        showWeekNumbers: true,
        locale: {
            buttons: {
                prev: '⟵',
                next: '⟶',
                close: 'x',
                reset: 'Zurücksetzen',
                apply: 'Anwenden',
            },
            tooltip: {
                one: 'Tag',
                other: 'Tage',
            },
            tooltipOnDisabled: null,
        },
        selectForward: true,
        onSelect: function(start, end){
            let str = '';
            startDate = start ? start.format('DD.MM.YYYY') + '' : '';
            str += start ? start.format('DD.MM.YYYY') + ' - ' : '';
            endDate = end ? end.format('DD.MM.YYYY') + '' : '';
            str += end ? end.format('DD.MM.YYYY') + '' : '';
            dateRangePicker.value = str;

            getDate(startDate, endDate);
        }
    });

    let dateRangePicker2 = document.getElementById('dateRangePicker2');
        let pickerRange2 = new Lightpick({
        field: dateRangePicker2,
        singleDate: false,
        lang: 'de',
        format: 'DD.MM.YYYY',
        disableWeekends: false,
        minDays: 6,
        maxDays: 6,
        weekdayStyle: 'long',
        showWeekNumbers: true,
        locale: {
            buttons: {
                prev: '⟵',
                next: '⟶',
                close: 'x',
                reset: 'Zurücksetzen',
                apply: 'Anwenden',
            },
            tooltip: {
                one: 'Tag',
                other: 'Tage',
            },
            tooltipOnDisabled: null,
        },
        selectForward: true,
        onSelect: function(start, end){
            let str = '';
            startDate = start ? start.format('DD.MM.YYYY') + '' : '';
            str += start ? start.format('DD.MM.YYYY') + ' - ' : '';
            endDate = end ? end.format('DD.MM.YYYY') + '' : '';
            str += end ? end.format('DD.MM.YYYY') + '' : '';
            dateRangePicker2.value = str;

            getDate(startDate, endDate);
        }
    });

    function getDate(startDate, endDate) {
        console.log('Von: ' + startDate);
        console.log('Bis: ' + endDate);

        startDate = startDate;
        endDate = endDate;
    };
});

// document.getElementById('submit-dateRange').onclick = function() {
    // var get = window.open('');
    // get.document.write('Von: ' + startDate + ', bis: ' + endDate)
    // document.getElementById('djangoDateRangePicker').value = 'Von: ' + startDate + ', bis: ' + endDate;
// };
