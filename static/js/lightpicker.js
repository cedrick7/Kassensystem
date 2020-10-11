/**
 * Minified by jsDelivr using Terser v3.14.1.
 * Original file: /npm/lightpick@1.3.4/lightpick.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
!(function (t, e) {
    if ("function" == typeof define && define.amd)
        define(["moment"], function (t) {
            return e(t);
        });
    else if ("object" == typeof module && module.exports) {
        var s = "undefined" != typeof window && void 0 !== window.moment ? window.moment : require("moment");
        module.exports = e(s);
    } else t.Lightpick = e(t.moment);
})(this, function (t) {
    "use strict";
    var e = window.document,
        s = {
            field: null,
            secondField: null,
            firstDay: 1,
            parentEl: "body",
            lang: "auto",
            format: "DD/MM/YYYY",
            separator: " - ",
            numberOfMonths: 1,
            numberOfColumns: 2,
            singleDate: !0,
            autoclose: !0,
            repick: !1,
            startDate: null,
            endDate: null,
            minDate: null,
            maxDate: null,
            disableDates: null,
            selectForward: !1,
            selectBackward: !1,
            minDays: null,
            maxDays: null,
            hoveringTooltip: !0,
            hideOnBodyClick: !0,
            footer: !1,
            disabledDatesInRange: !0,
            tooltipNights: !1,
            orientation: "auto",
            disableWeekends: !1,
            inline: !1,
            dropdowns: { years: { min: 1900, max: null }, months: !0 },
            locale: {
                buttons: { prev: "&leftarrow;", next: "&rightarrow;", close: "&times;", reset: "Reset", apply: "Apply" },
                tooltip: { one: "day", other: "days" },
                tooltipOnDisabled: null,
                pluralize: function (t, e) {
                    return "string" == typeof t && (t = parseInt(t, 10)), 1 === t && "one" in e ? e.one : "other" in e ? e.other : "";
                },
            },
            onSelect: null,
            onOpen: null,
            onClose: null,
            onError: null,
        },
        i = function (t) {
            return (
                '<div class="lightpick__toolbar"><button type="button" class="lightpick__previous-action">' +
                t.locale.buttons.prev +
                '</button><button type="button" class="lightpick__next-action">' +
                t.locale.buttons.next +
                "</button>" +
                (t.autoclose || t.inline ? "" : '<button type="button" class="lightpick__close-action">' + t.locale.buttons.close + "</button>") +
                "</div>"
            );
        },
        a = function (t, e, s) {
            return new Date(1970, 0, e).toLocaleString(t.lang, { weekday: s ? "short" : "long" });
        },
        n = function (s, i, a, n) {
            if (a) return "<div></div>";
            i = t(i);
            var o = t(i).subtract(1, "month"),
                l = t(i).add(1, "month"),
                r = { time: t(i).valueOf(), className: ["lightpick__day", "is-available"] };
            if (
                (n instanceof Array || "[object Array]" === Object.prototype.toString.call(n)
                    ? ((n = n.filter(function (t) {
                          return ["lightpick__day", "is-available", "is-previous-month", "is-next-month"].indexOf(t) >= 0;
                      })),
                      (r.className = r.className.concat(n)))
                    : r.className.push(n),
                s.disableDates)
            )
                for (var d = 0; d < s.disableDates.length; d++) {
                    if (s.disableDates[d] instanceof Array || "[object Array]" === Object.prototype.toString.call(s.disableDates[d])) {
                        var c = t(s.disableDates[d][0]),
                            h = t(s.disableDates[d][1]);
                        c.isValid() && h.isValid() && i.isBetween(c, h, "day", "[]") && r.className.push("is-disabled");
                    } else t(s.disableDates[d]).isValid() && t(s.disableDates[d]).isSame(i, "day") && r.className.push("is-disabled");
                    r.className.indexOf("is-disabled") >= 0 &&
                        (s.locale.tooltipOnDisabled && (!s.startDate || i.isAfter(s.startDate) || (s.startDate && s.endDate)) && r.className.push("disabled-tooltip"),
                        r.className.indexOf("is-start-date") >= 0 ? (this.setStartDate(null), this.setEndDate(null)) : r.className.indexOf("is-end-date") >= 0 && this.setEndDate(null));
                }
            if (
                (s.minDays &&
                    s.startDate &&
                    !s.endDate &&
                    i.isBetween(t(s.startDate).subtract(s.minDays - 1, "day"), t(s.startDate).add(s.minDays - 1, "day"), "day") &&
                    (r.className.push("is-disabled"), s.selectForward && i.isSameOrAfter(s.startDate) && (r.className.push("is-forward-selected"), r.className.push("is-in-range"))),
                s.maxDays &&
                    s.startDate &&
                    !s.endDate &&
                    (i.isSameOrBefore(t(s.startDate).subtract(s.maxDays, "day"), "day") ? r.className.push("is-disabled") : i.isSameOrAfter(t(s.startDate).add(s.maxDays, "day"), "day") && r.className.push("is-disabled")),
                s.repick && (s.minDays || s.maxDays) && s.startDate && s.endDate)
            ) {
                var p = t(s.repickTrigger == s.field ? s.endDate : s.startDate);
                s.minDays && i.isBetween(t(p).subtract(s.minDays - 1, "day"), t(p).add(s.minDays - 1, "day"), "day") && r.className.push("is-disabled"),
                    s.maxDays && (i.isSameOrBefore(t(p).subtract(s.maxDays, "day"), "day") ? r.className.push("is-disabled") : i.isSameOrAfter(t(p).add(s.maxDays, "day"), "day") && r.className.push("is-disabled"));
            }
            i.isSame(new Date(), "day") && r.className.push("is-today"),
                i.isSame(s.startDate, "day") && r.className.push("is-start-date"),
                i.isSame(s.endDate, "day") && r.className.push("is-end-date"),
                s.startDate && s.endDate && i.isBetween(s.startDate, s.endDate, "day", "[]") && r.className.push("is-in-range"),
                t().isSame(i, "month") || (o.isSame(i, "month") ? r.className.push("is-previous-month") : l.isSame(i, "month") && r.className.push("is-next-month")),
                s.minDate && i.isBefore(s.minDate, "day") && r.className.push("is-disabled"),
                s.maxDate && i.isAfter(s.maxDate, "day") && r.className.push("is-disabled"),
                s.selectForward && !s.singleDate && s.startDate && !s.endDate && i.isBefore(s.startDate, "day") && r.className.push("is-disabled"),
                s.selectBackward && !s.singleDate && s.startDate && !s.endDate && i.isAfter(s.startDate, "day") && r.className.push("is-disabled"),
                !s.disableWeekends || (6 != i.isoWeekday() && 7 != i.isoWeekday()) || r.className.push("is-disabled"),
                (r.className = r.className.filter(function (t, e, s) {
                    return s.indexOf(t) === e;
                })),
                r.className.indexOf("is-disabled") >= 0 && r.className.indexOf("is-available") >= 0 && r.className.splice(r.className.indexOf("is-available"), 1);
            var u = e.createElement("div");
            return (u.className = r.className.join(" ")), (u.innerHTML = i.get("date")), u.setAttribute("data-time", r.time), u.outerHTML;
        },
        o = function (s, i) {
            for (var a = t(s), n = e.createElement("select"), o = 0; o < 12; o++) {
                a.set("month", o);
                var l = e.createElement("option");
                (l.value = a.toDate().getMonth()), (l.text = a.toDate().toLocaleString(i.lang, { month: "long" })), o === s.toDate().getMonth() && l.setAttribute("selected", "selected"), n.appendChild(l);
            }
            return (n.className = "lightpick__select lightpick__select-months"), (n.dir = "rtl"), (i.dropdowns && i.dropdowns.months) || (n.disabled = !0), n.outerHTML;
        },
        l = function (s, i) {
            var a = t(s),
                n = e.createElement("select"),
                o = i.dropdowns && i.dropdowns.years ? i.dropdowns.years : null,
                l = o && o.min ? o.min : 1900,
                r = o && o.max ? o.max : Number.parseInt(t().format("YYYY"));
            Number.parseInt(s.format("YYYY")) < l && (l = Number.parseInt(s.format("YYYY"))), Number.parseInt(s.format("YYYY")) > r && (r = Number.parseInt(s.format("YYYY")));
            for (var d = l; d <= r; d++) {
                a.set("year", d);
                var c = e.createElement("option");
                (c.value = a.toDate().getFullYear()), (c.text = a.toDate().getFullYear()), d === s.toDate().getFullYear() && c.setAttribute("selected", "selected"), n.appendChild(c);
            }
            return (n.className = "lightpick__select lightpick__select-years"), (i.dropdowns && i.dropdowns.years) || (n.disabled = !0), n.outerHTML;
        },
        r = function (e, s) {
            for (var r = "", d = t(s.calendar[0]), c = 0; c < s.numberOfMonths; c++) {
                var h = t(d);
                (r += '<section class="lightpick__month">'),
                    (r += '<header class="lightpick__month-title-bar">'),
                    (r += '<div class="lightpick__month-title">' + o(h, s) + l(h, s) + "</div>"),
                    1 === s.numberOfMonths && (r += i(s)),
                    (r += "</header>"),
                    (r += '<div class="lightpick__days-of-the-week">');
                for (var p = s.firstDay + 4; p < 7 + s.firstDay + 4; ++p) r += '<div class="lightpick__day-of-the-week" title="' + a(s, p) + '">' + a(s, p, !0) + "</div>";
                if (((r += "</div>"), (r += '<div class="lightpick__days">'), h.isoWeekday() !== s.firstDay))
                    for (var u = h.isoWeekday() - s.firstDay > 0 ? h.isoWeekday() - s.firstDay : h.isoWeekday(), f = t(h).subtract(u, "day"), _ = f.daysInMonth(), m = f.get("date"); m <= _; m++)
                        (r += n(s, f, c > 0, "is-previous-month")), f.add(1, "day");
                for (_ = h.daysInMonth(), new Date(), m = 0; m < _; m++) (r += n(s, h)), h.add(1, "day");
                var D = t(h),
                    g = 7 - D.isoWeekday() + s.firstDay;
                if (g < 7) for (m = D.get("date"); m <= g; m++) (r += n(s, D, c < s.numberOfMonths - 1, "is-next-month")), D.add(1, "day");
                (r += "</div>"), (r += "</section>"), d.add(1, "month");
            }
            (s.calendar[1] = t(d)), (e.querySelector(".lightpick__months").innerHTML = r);
        },
        d = function (t, e) {
            var s = t.querySelectorAll(".lightpick__day");
            [].forEach.call(s, function (t) {
                t.outerHTML = n(e, parseInt(t.getAttribute("data-time")), !1, t.className.split(" "));
            }),
                c(t, e);
        },
        c = function (e, s) {
            if (!s.disabledDatesInRange && s.startDate && !s.endDate && s.disableDates) {
                var i = e.querySelectorAll(".lightpick__day"),
                    a = s.disableDates.map(function (t) {
                        return t instanceof Array || "[object Array]" === Object.prototype.toString.call(t) ? t[0] : t;
                    }),
                    n = t(
                        a
                            .filter(function (e) {
                                return t(e).isBefore(s.startDate);
                            })
                            .sort(function (e, s) {
                                return t(s).isAfter(t(e));
                            })[0]
                    ),
                    o = t(
                        a
                            .filter(function (e) {
                                return t(e).isAfter(s.startDate);
                            })
                            .sort(function (e, s) {
                                return t(e).isAfter(t(s));
                            })[0]
                    );
                [].forEach.call(i, function (e) {
                    var i = t(parseInt(e.getAttribute("data-time")));
                    ((n && i.isBefore(n) && s.startDate.isAfter(n)) || (o && i.isAfter(o) && o.isAfter(s.startDate))) && (e.classList.remove("is-available"), e.classList.add("is-disabled"));
                });
            }
        },
        h = function (s) {
            var a = this,
                n = a.config(s);
            (a.el = e.createElement("section")), (a.el.className = "lightpick lightpick--" + n.numberOfColumns + "-columns is-hidden"), n.inline && (a.el.className += " lightpick--inlined");
            var o = '<div class="lightpick__inner">' + (n.numberOfMonths > 1 ? i(n) : "") + '<div class="lightpick__months"></div><div class="lightpick__tooltip" style="visibility: hidden"></div>';
            n.footer &&
                ((o += '<div class="lightpick__footer">'),
                !0 === n.footer
                    ? ((o += '<button type="button" class="lightpick__reset-action">' + n.locale.buttons.reset + "</button>"),
                      (o += '<div class="lightpick__footer-message"></div>'),
                      (o += '<button type="button" class="lightpick__apply-action">' + n.locale.buttons.apply + "</button>"))
                    : (o += n.footer),
                (o += "</div>")),
                (o += "</div>"),
                (a.el.innerHTML = o),
                n.parentEl instanceof Node ? n.parentEl.appendChild(a.el) : "body" === n.parentEl && n.inline ? n.field.parentNode.appendChild(a.el) : e.querySelector(n.parentEl).appendChild(a.el),
                (a._onMouseDown = function (e) {
                    if (a.isShowing) {
                        var s = (e = e || window.event).target || e.srcElement;
                        if (s) {
                            e.stopPropagation(), s.classList.contains("lightpick__select") || e.preventDefault();
                            var i = a._opts;
                            if (s.classList.contains("lightpick__day") && s.classList.contains("is-available")) {
                                var n = t(parseInt(s.getAttribute("data-time")));
                                if (!i.disabledDatesInRange && i.disableDates && i.startDate) {
                                    var o = n.isAfter(i.startDate) ? t(i.startDate) : t(n),
                                        l = n.isAfter(i.startDate) ? t(n) : t(i.startDate);
                                    if (
                                        i.disableDates.filter(function (e) {
                                            if (e instanceof Array || "[object Array]" === Object.prototype.toString.call(e)) {
                                                var s = t(e[0]),
                                                    i = t(e[1]);
                                                return s.isValid() && i.isValid() && (s.isBetween(o, l, "day", "[]") || i.isBetween(o, l, "day", "[]"));
                                            }
                                            return t(e).isBetween(o, l, "day", "[]");
                                        }).length
                                    )
                                        return a.setStartDate(null), a.setEndDate(null), s.dispatchEvent(new Event("mousedown")), (a.el.querySelector(".lightpick__tooltip").style.visibility = "hidden"), void d(a.el, i);
                                }
                                if (
                                    (i.singleDate || (!i.startDate && !i.endDate) || (i.startDate && i.endDate)
                                        ? i.repick && i.startDate && i.endDate
                                            ? (i.repickTrigger === i.field ? (a.setStartDate(n), s.classList.add("is-start-date")) : (a.setEndDate(n), s.classList.add("is-end-date")),
                                              i.startDate.isAfter(i.endDate) && a.swapDate(),
                                              i.autoclose &&
                                                  setTimeout(function () {
                                                      a.hide();
                                                  }, 100))
                                            : (a.setStartDate(n),
                                              a.setEndDate(null),
                                              s.classList.add("is-start-date"),
                                              i.singleDate && i.autoclose
                                                  ? setTimeout(function () {
                                                        a.hide();
                                                    }, 100)
                                                  : (i.singleDate && !i.inline) || d(a.el, i))
                                        : i.startDate &&
                                          !i.endDate &&
                                          (a.setEndDate(n),
                                          i.startDate.isAfter(i.endDate) && a.swapDate(),
                                          s.classList.add("is-end-date"),
                                          i.autoclose
                                              ? setTimeout(function () {
                                                    a.hide();
                                                }, 100)
                                              : d(a.el, i)),
                                    !i.disabledDatesInRange && 0 === a.el.querySelectorAll(".lightpick__day.is-available").length && (a.setStartDate(null), d(a.el, i), i.footer))
                                )
                                    if ("function" == typeof a._opts.onError) a._opts.onError.call(a, "Invalid range");
                                    else {
                                        var r = a.el.querySelector(".lightpick__footer-message");
                                        r &&
                                            ((r.innerHTML = i.locale.not_allowed_range),
                                            setTimeout(function () {
                                                r.innerHTML = "";
                                            }, 3e3));
                                    }
                            } else
                                s.classList.contains("lightpick__previous-action")
                                    ? a.prevMonth()
                                    : s.classList.contains("lightpick__next-action")
                                    ? a.nextMonth()
                                    : s.classList.contains("lightpick__close-action") || s.classList.contains("lightpick__apply-action")
                                    ? a.hide()
                                    : s.classList.contains("lightpick__reset-action") && a.reset();
                        }
                    }
                }),
                (a._onMouseEnter = function (e) {
                    if (a.isShowing) {
                        var s = (e = e || window.event).target || e.srcElement;
                        if (s) {
                            var i = a._opts;
                            if (s.classList.contains("lightpick__day") && s.classList.contains("disabled-tooltip") && i.locale.tooltipOnDisabled) a.showTooltip(s, i.locale.tooltipOnDisabled);
                            else if ((a.hideTooltip(), !i.singleDate && (i.startDate || i.endDate) && (s.classList.contains("lightpick__day") || s.classList.contains("is-available")) && ((i.startDate && !i.endDate) || i.repick))) {
                                var n = t(parseInt(s.getAttribute("data-time")));
                                if (!n.isValid()) return;
                                var o = (i.startDate && !i.endDate) || (i.repick && i.repickTrigger === i.secondField) ? i.startDate : i.endDate,
                                    l = a.el.querySelectorAll(".lightpick__day");
                                if (
                                    ([].forEach.call(l, function (e) {
                                        var s = t(parseInt(e.getAttribute("data-time")));
                                        e.classList.remove("is-flipped"),
                                            s.isValid() && s.isSameOrAfter(o, "day") && s.isSameOrBefore(n, "day")
                                                ? (e.classList.add("is-in-range"), i.repickTrigger === i.field && s.isSameOrAfter(i.endDate) && e.classList.add("is-flipped"))
                                                : s.isValid() && s.isSameOrAfter(n, "day") && s.isSameOrBefore(o, "day")
                                                ? (e.classList.add("is-in-range"), ((i.startDate && !i.endDate) || i.repickTrigger === i.secondField) && s.isSameOrBefore(i.startDate) && e.classList.add("is-flipped"))
                                                : e.classList.remove("is-in-range"),
                                            i.startDate && i.endDate && i.repick && i.repickTrigger === i.field ? e.classList.remove("is-start-date") : e.classList.remove("is-end-date");
                                    }),
                                    i.hoveringTooltip)
                                ) {
                                    (l = Math.abs(n.isAfter(o) ? n.diff(o, "day") : o.diff(n, "day"))), i.tooltipNights || (l += 1);
                                    a.el.querySelector(".lightpick__tooltip");
                                    if (l > 0 && !s.classList.contains("is-disabled")) {
                                        var r = "";
                                        "function" == typeof i.locale.pluralize && (r = i.locale.pluralize.call(a, l, i.locale.tooltip)), a.showTooltip(s, l + " " + r);
                                    } else a.hideTooltip();
                                }
                                i.startDate && i.endDate && i.repick && i.repickTrigger === i.field ? s.classList.add("is-start-date") : s.classList.add("is-end-date");
                            }
                        }
                    }
                }),
                (a._onChange = function (t) {
                    var e = (t = t || window.event).target || t.srcElement;
                    e && (e.classList.contains("lightpick__select-months") ? a.gotoMonth(e.value) : e.classList.contains("lightpick__select-years") && a.gotoYear(e.value));
                }),
                (a._onInputChange = function (t) {
                    t.target || t.srcElement;
                    a._opts.singleDate && (a._opts.autoclose || a.gotoDate(n.field.value)), a.syncFields(), a.isShowing || a.show();
                }),
                (a._onInputFocus = function (t) {
                    var e = t.target || t.srcElement;
                    a.show(e);
                }),
                (a._onInputClick = function (t) {
                    var e = t.target || t.srcElement;
                    a.show(e);
                }),
                (a._onClick = function (t) {
                    var e = (t = t || window.event).target || t.srcElement,
                        s = e;
                    if (e) {
                        do {
                            if ((s.classList && s.classList.contains("lightpick")) || s === n.field || (n.secondField && s === n.secondField)) return;
                        } while ((s = s.parentNode));
                        a.isShowing && n.hideOnBodyClick && e !== n.field && s !== n.field && a.hide();
                    }
                }),
                (a.showTooltip = function (t, e) {
                    var s = a.el.querySelector(".lightpick__tooltip"),
                        i = a.el.classList.contains("lightpick--inlined"),
                        n = t.getBoundingClientRect(),
                        o = i ? a.el.parentNode.getBoundingClientRect() : a.el.getBoundingClientRect(),
                        l = n.left - o.left + n.width / 2,
                        r = n.top - o.top;
                    (s.style.visibility = "visible"), (s.textContent = e);
                    var d = s.getBoundingClientRect();
                    (r -= d.height),
                        (l -= d.width / 2),
                        setTimeout(function () {
                            (s.style.top = r + "px"), (s.style.left = l + "px");
                        }, 10);
                }),
                (a.hideTooltip = function () {
                    a.el.querySelector(".lightpick__tooltip").style.visibility = "hidden";
                }),
                a.el.addEventListener("mousedown", a._onMouseDown, !0),
                a.el.addEventListener("mouseenter", a._onMouseEnter, !0),
                a.el.addEventListener("touchend", a._onMouseDown, !0),
                a.el.addEventListener("change", a._onChange, !0),
                n.inline ? a.show() : a.hide(),
                n.field.addEventListener("change", a._onInputChange),
                n.field.addEventListener("click", a._onInputClick),
                n.field.addEventListener("focus", a._onInputFocus),
                n.secondField && (n.secondField.addEventListener("change", a._onInputChange), n.secondField.addEventListener("click", a._onInputClick), n.secondField.addEventListener("focus", a._onInputFocus));
        };
    return (
        (h.prototype = {
            config: function (e) {
                var i = Object.assign({}, s, e);
                if (
                    ((i.field = i.field && i.field.nodeName ? i.field : null),
                    (i.calendar = [t().set("date", 1)]),
                    1 === i.numberOfMonths && i.numberOfColumns > 1 && (i.numberOfColumns = 1),
                    (i.minDate = i.minDate && t(i.minDate).isValid() ? t(i.minDate) : null),
                    (i.maxDate = i.maxDate && t(i.maxDate).isValid() ? t(i.maxDate) : null),
                    "auto" === i.lang)
                ) {
                    var a = navigator.language || navigator.userLanguage;
                    i.lang = a || "en-US";
                }
                return (
                    i.secondField && i.singleDate && (i.singleDate = !1),
                    i.hoveringTooltip && i.singleDate && (i.hoveringTooltip = !1),
                    "[object Object]" === Object.prototype.toString.call(e.locale) && (i.locale = Object.assign({}, s.locale, e.locale)),
                    window.innerWidth < 480 && i.numberOfMonths > 1 && ((i.numberOfMonths = 1), (i.numberOfColumns = 1)),
                    i.repick && !i.secondField && (i.repick = !1),
                    i.inline && ((i.autoclose = !1), (i.hideOnBodyClick = !1)),
                    (this._opts = Object.assign({}, i)),
                    this.syncFields(),
                    this.setStartDate(this._opts.startDate, !0),
                    this.setEndDate(this._opts.endDate, !0),
                    this._opts
                );
            },
            syncFields: function () {
                if (this._opts.singleDate || this._opts.secondField)
                    t(this._opts.field.value, this._opts.format).isValid() && (this._opts.startDate = t(this._opts.field.value, this._opts.format)),
                        this._opts.secondField && t(this._opts.secondField.value, this._opts.format).isValid() && (this._opts.endDate = t(this._opts.secondField.value, this._opts.format));
                else {
                    var e = this._opts.field.value.split(this._opts.separator);
                    2 === e.length && (t(e[0], this._opts.format).isValid() && (this._opts.startDate = t(e[0], this._opts.format)), t(e[1], this._opts.format).isValid() && (this._opts.endDate = t(e[1], this._opts.format)));
                }
            },
            swapDate: function () {
                var e = t(this._opts.startDate);
                this.setDateRange(this._opts.endDate, e);
            },
            gotoToday: function () {
                this.gotoDate(new Date());
            },
            gotoDate: function (e) {
                (e = t(e)).isValid() || (e = t()), e.set("date", 1), (this._opts.calendar = [t(e)]), r(this.el, this._opts);
            },
            gotoMonth: function (t) {
                isNaN(t) || (this._opts.calendar[0].set("month", t), r(this.el, this._opts));
            },
            gotoYear: function (t) {
                isNaN(t) || (this._opts.calendar[0].set("year", t), r(this.el, this._opts));
            },
            prevMonth: function () {
                (this._opts.calendar[0] = t(this._opts.calendar[0]).subtract(this._opts.numberOfMonths, "month")), r(this.el, this._opts), c(this.el, this._opts);
            },
            nextMonth: function () {
                (this._opts.calendar[0] = t(this._opts.calendar[1])), r(this.el, this._opts), c(this.el, this._opts);
            },
            updatePosition: function () {
                if (!this.el.classList.contains("lightpick--inlined")) {
                    this.el.classList.remove("is-hidden");
                    var t = this._opts.field.getBoundingClientRect(),
                        e = this.el.getBoundingClientRect(),
                        s = this._opts.orientation.split(" "),
                        i = 0,
                        a = 0;
                    "auto" != s[0] && /top|bottom/.test(s[0])
                        ? ((i = t[s[0]] + window.pageYOffset), "top" == s[0] && (i -= e.height))
                        : (i = t.bottom + e.height > window.innerHeight && window.pageYOffset > e.height ? t.top + window.pageYOffset - e.height : t.bottom + window.pageYOffset),
                        /left|right/.test(s[0]) || (s[1] && "auto" != s[1] && /left|right/.test(s[1]))
                            ? ((a = /left|right/.test(s[0]) ? t[s[0]] + window.pageXOffset : t[s[1]] + window.pageXOffset), ("right" != s[0] && "right" != s[1]) || (a -= e.width))
                            : (a = t.left + e.width > window.innerWidth ? t.right + window.pageXOffset - e.width : t.left + window.pageXOffset),
                        this.el.classList.add("is-hidden"),
                        (this.el.style.top = i + "px"),
                        (this.el.style.left = a + "px");
                }
            },
            setStartDate: function (e, s) {
                var i = t(e, t.ISO_8601),
                    a = t(e, this._opts.format);
                if (!i.isValid() && !a.isValid()) return (this._opts.startDate = null), void (this._opts.field.value = "");
                (this._opts.startDate = t(i.isValid() ? i : a)),
                    this._opts.singleDate || this._opts.secondField
                        ? (this._opts.field.value = this._opts.startDate.format(this._opts.format))
                        : (this._opts.field.value = this._opts.startDate.format(this._opts.format) + this._opts.separator + "..."),
                    s || "function" != typeof this._opts.onSelect || this._opts.onSelect.call(this, this.getStartDate(), this.getEndDate());
            },
            setEndDate: function (e, s) {
                var i = t(e, t.ISO_8601),
                    a = t(e, this._opts.format);
                if (!i.isValid() && !a.isValid())
                    return (
                        (this._opts.endDate = null),
                        void (this._opts.secondField
                            ? (this._opts.secondField.value = "")
                            : !this._opts.singleDate && this._opts.startDate && (this._opts.field.value = this._opts.startDate.format(this._opts.format) + this._opts.separator + "..."))
                    );
                (this._opts.endDate = t(i.isValid() ? i : a)),
                    this._opts.secondField
                        ? ((this._opts.field.value = this._opts.startDate.format(this._opts.format)), (this._opts.secondField.value = this._opts.endDate.format(this._opts.format)))
                        : (this._opts.field.value = this._opts.startDate.format(this._opts.format) + this._opts.separator + this._opts.endDate.format(this._opts.format)),
                    s || "function" != typeof this._opts.onSelect || this._opts.onSelect.call(this, this.getStartDate(), this.getEndDate());
            },
            setDate: function (t, e) {
                this._opts.singleDate && (this.setStartDate(t, e), this.isShowing && d(this.el, this._opts));
            },
            setDateRange: function (t, e, s) {
                this._opts.singleDate ||
                    (this.setStartDate(t, !0), this.setEndDate(e, !0), this.isShowing && d(this.el, this._opts), s || "function" != typeof this._opts.onSelect || this._opts.onSelect.call(this, this.getStartDate(), this.getEndDate()));
            },
            setDisableDates: function (t) {
                (this._opts.disableDates = t), this.isShowing && d(this.el, this._opts);
            },
            getStartDate: function () {
                return t(this._opts.startDate).isValid() ? this._opts.startDate : null;
            },
            getEndDate: function () {
                return t(this._opts.endDate).isValid() ? this._opts.endDate : null;
            },
            getDate: function () {
                return t(this._opts.startDate).isValid() ? this._opts.startDate : null;
            },
            toString: function (e) {
                return this._opts.singleDate
                    ? t(this._opts.startDate).isValid()
                        ? this._opts.startDate.format(e)
                        : ""
                    : t(this._opts.startDate).isValid() && t(this._opts.endDate).isValid()
                    ? this._opts.startDate.format(e) + this._opts.separator + this._opts.endDate.format(e)
                    : t(this._opts.startDate).isValid() && !t(this._opts.endDate).isValid()
                    ? this._opts.startDate.format(e) + this._opts.separator + "..."
                    : !t(this._opts.startDate).isValid() && t(this._opts.endDate).isValid()
                    ? "..." + this._opts.separator + this._opts.endDate.format(e)
                    : "";
            },
            show: function (t) {
                this.isShowing ||
                    ((this.isShowing = !0),
                    this._opts.repick && (this._opts.repickTrigger = t),
                    this.syncFields(),
                    this._opts.secondField && this._opts.secondField === t && this._opts.endDate ? this.gotoDate(this._opts.endDate) : this.gotoDate(this._opts.startDate),
                    e.addEventListener("click", this._onClick),
                    this.updatePosition(),
                    this.el.classList.remove("is-hidden"),
                    "function" == typeof this._opts.onOpen && this._opts.onOpen.call(this),
                    e.activeElement && e.activeElement != e.body && e.activeElement.blur());
            },
            hide: function () {
                this.isShowing &&
                    ((this.isShowing = !1),
                    e.removeEventListener("click", this._onClick),
                    this.el.classList.add("is-hidden"),
                    (this.el.querySelector(".lightpick__tooltip").style.visibility = "hidden"),
                    "function" == typeof this._opts.onClose && this._opts.onClose.call(this));
            },
            destroy: function () {
                var t = this._opts;
                this.hide(),
                    this.el.removeEventListener("mousedown", self._onMouseDown, !0),
                    this.el.removeEventListener("mouseenter", self._onMouseEnter, !0),
                    this.el.removeEventListener("touchend", self._onMouseDown, !0),
                    this.el.removeEventListener("change", self._onChange, !0),
                    t.field.removeEventListener("change", this._onInputChange),
                    t.field.removeEventListener("click", this._onInputClick),
                    t.field.removeEventListener("focus", this._onInputFocus),
                    t.secondField && (t.secondField.removeEventListener("change", this._onInputChange), t.secondField.removeEventListener("click", this._onInputClick), t.secondField.removeEventListener("focus", this._onInputFocus)),
                    this.el.parentNode && this.el.parentNode.removeChild(this.el);
            },
            reset: function () {
                this.setStartDate(null, !0),
                    this.setEndDate(null, !0),
                    d(this.el, this._opts),
                    "function" == typeof this._opts.onSelect && this._opts.onSelect.call(this, this.getStartDate(), this.getEndDate()),
                    (this.el.querySelector(".lightpick__tooltip").style.visibility = "hidden");
            },
            reloadOptions: function (t) {
                this._opts = Object.assign({}, this._opts, t);
            },
        }),
        h
    );
});
//# sourceMappingURL=/sm/c4134b711a4490a1339f56150dfaa86a9670d67329c90b95f1be6522417244c0.map

