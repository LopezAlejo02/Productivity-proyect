//Colors    
var axixs_colors = "#000000"
//Chart Options
var options_bar = {
    chart: {
        type: 'bar'
    },
    plotOptions: {
        bar: {
        distributed: true
        }},
    series: [{
      name: 'tasks',
      data: tasks
    }],
    xaxis: {
      labels: {
        style: {
        }
      },
      categories: projects
    },
    theme: {
        mode: 'dark', 
        palette: 'palette1', 
        monochrome: {
            enabled: false,
            color: '#255aee',
            shadeTo: 'light',
            shadeIntensity: 0.65
        },
    },
    legend: {
        show: false
    }
  }
  
  //Init chart
  var chart_bar = new ApexCharts(document.querySelector("#chart_bar"), options_bar);
  

  //Render chart
  chart_bar.render();

//Chart Options
var options_donut = {
    series: tasks,
    labels: projects,
    chart: {
    type: 'donut',
  },
  plotOptions: {
    pie: {
      expandOnClick: false
    }
  },
  theme: {
    mode: 'dark', 
    palette: 'palette1', 
    monochrome: {
        enabled: false,
        color: '#255aee',
        shadeTo: 'light',
        shadeIntensity: 0.65
    },
},
  responsive: [{
    breakpoint: 480,
    options: {
      chart: {
        width: 200
      },
      legend: {
        position: 'bottom'
      }
    }
  }]
  };

  //Init chart
var chart_donut = new ApexCharts(document.querySelector("#chart_donut"), options_donut);

//Render chart
chart_donut.render();