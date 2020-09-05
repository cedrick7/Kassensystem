$(function(){
    let dateRangePicker = document.getElementById('dateRangePicker');
        let pickerRange = new Lightpick({
        field: dateRangePicker,
        singleDate: false,
        onSelect: function(start, end){
            let str = '';
            str += start ? start.format('Do MMMM YYYY') + ' bis ' : '';
            str += end ? end.format('Do MMMM YYYY') : '...';
            dateRangePicker.value = str;
        }
    });
});
