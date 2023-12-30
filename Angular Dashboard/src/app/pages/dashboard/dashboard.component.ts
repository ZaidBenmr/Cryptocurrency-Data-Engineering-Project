import { Component, OnInit } from "@angular/core";
import Chart from 'chart.js';
import { ApiService } from '../../api.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: "app-dashboard",
  templateUrl: "dashboard.component.html",
  providers : [ApiService]
})
export class DashboardComponent implements OnInit {
  public canvas : any;
  public ctx;
  public datasets: any;
  public data: any;
  public myChartData;
  public clicked: boolean = true;
  public clicked1: boolean = false;
  public clicked2: boolean = false;
  public clicked3: boolean = false;
  public clicked0: boolean = true;
  public clicked11: boolean = false;
  public clicked22: boolean = false;
  public clicked33: boolean = false;
  data_coins : any
  open : any
  high : any
  low : any
  close : any
  adj_close : any
  date : any
  return_dates : any
  returns : any
  correlation : any
  volatilty : any
  garde1 : string = "btc"
  garde2 : any = 0
  garde3 : any = 0
  selectedCandel : any = "Bitcoin"
  selectedReturn : any = "Bitcoin"
  selectedHistg  : any = "Bitcoin"

  candelgraph : any
  closeprice : any
  histograme : any
  returnsgraph : any
  correlationgraph : any
  cumreturnsgraph : any
  volatiltygraph : any

  constructor(private api:  ApiService,private toastr: ToastrService) {
    this.getAllData();
    this.Returns();
    this.getCorrelation();
    this.getVolatilty();
    //this.showNotification('top','center');
  }

  ngOnInit() {
    var gradientChartOptionsConfigurationWithTooltipBlue: any = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 60,
            suggestedMax: 125,
            padding: 20,
            fontColor: "#2380f7"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#2380f7"
          }
        }]
      }
    };

    var gradientChartOptionsConfigurationWithTooltipPurple: any = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 60,
            suggestedMax: 125,
            padding: 20,
            fontColor: "#9a9a9a"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(225,78,202,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9a9a9a"
          }
        }]
      }
    };

    var gradientChartOptionsConfigurationWithTooltipRed: any = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 60,
            suggestedMax: 125,
            padding: 20,
            fontColor: "#9a9a9a"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(233,32,16,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9a9a9a"
          }
        }]
      }
    };

    var gradientChartOptionsConfigurationWithTooltipOrange: any = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 50,
            suggestedMax: 110,
            padding: 20,
            fontColor: "#ff8a76"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(220,53,69,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#ff8a76"
          }
        }]
      }
    };

    var gradientChartOptionsConfigurationWithTooltipGreen: any = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 50,
            suggestedMax: 125,
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(0,242,195,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }]
      }
    };


    var gradientBarChartConfiguration: any = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{

          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 60,
            suggestedMax: 120,
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }],

        xAxes: [{

          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }]
      }
    };

    this.canvas = document.getElementById("chartLineRed");
    this.ctx = this.canvas.getContext("2d");

    var gradientStroke = this.ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(233,32,16,0.2)');
    gradientStroke.addColorStop(0.4, 'rgba(233,32,16,0.0)');
    gradientStroke.addColorStop(0, 'rgba(233,32,16,0)'); //red colors

    var data = {
      labels: ['JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
      datasets: [{
        label: "Data",
        fill: true,
        backgroundColor: gradientStroke,
        borderColor: '#ec250d',
        borderWidth: 2,
        borderDash: [],
        borderDashOffset: 0.0,
        pointBackgroundColor: '#ec250d',
        pointBorderColor: 'rgba(255,255,255,0)',
        pointHoverBackgroundColor: '#ec250d',
        pointBorderWidth: 20,
        pointHoverRadius: 4,
        pointHoverBorderWidth: 15,
        pointRadius: 4,
        data: [80, 100, 70, 80, 120, 80],
      }]
    };

    var myChart = new Chart(this.ctx, {
      type: 'line',
      data: data,
      options: gradientChartOptionsConfigurationWithTooltipRed
    });


    this.canvas = document.getElementById("chartLineGreen");
    this.ctx = this.canvas.getContext("2d");


    var gradientStroke = this.ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(66,134,121,0.15)');
    gradientStroke.addColorStop(0.4, 'rgba(66,134,121,0.0)'); //green colors
    gradientStroke.addColorStop(0, 'rgba(66,134,121,0)'); //green colors

    var data = {
      labels: ['JUL', 'AUG', 'SEP', 'OCT', 'NOV'],
      datasets: [{
        label: "My First dataset",
        fill: true,
        backgroundColor: gradientStroke,
        borderColor: '#00d6b4',
        borderWidth: 2,
        borderDash: [],
        borderDashOffset: 0.0,
        pointBackgroundColor: '#00d6b4',
        pointBorderColor: 'rgba(255,255,255,0)',
        pointHoverBackgroundColor: '#00d6b4',
        pointBorderWidth: 20,
        pointHoverRadius: 4,
        pointHoverBorderWidth: 15,
        pointRadius: 4,
        data: [90, 27, 60, 12, 80],
      }]
    };

    var myChart = new Chart(this.ctx, {
      type: 'line',
      data: data,
      options: gradientChartOptionsConfigurationWithTooltipGreen

    });



    var chart_labels = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'];
    this.datasets = [
      [100, 70, 90, 70, 85, 60, 75, 60, 90, 80, 110, 100],
      [80, 120, 105, 110, 95, 105, 90, 100, 80, 95, 70, 120],
      [60, 80, 65, 130, 80, 105, 90, 130, 70, 115, 60, 130]
    ];
    this.data = this.datasets[0];



    this.canvas = document.getElementById("chartBig1");
    this.ctx = this.canvas.getContext("2d");

    var gradientStroke = this.ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(233,32,16,0.2)');
    gradientStroke.addColorStop(0.4, 'rgba(233,32,16,0.0)');
    gradientStroke.addColorStop(0, 'rgba(233,32,16,0)'); //red colors

    var config = {
      type: 'line',
      data: {
        labels: chart_labels,
        datasets: [{
          label: "My First dataset",
          fill: true,
          backgroundColor: gradientStroke,
          borderColor: '#ec250d',
          borderWidth: 2,
          borderDash: [],
          borderDashOffset: 0.0,
          pointBackgroundColor: '#ec250d',
          pointBorderColor: 'rgba(255,255,255,0)',
          pointHoverBackgroundColor: '#ec250d',
          pointBorderWidth: 20,
          pointHoverRadius: 4,
          pointHoverBorderWidth: 15,
          pointRadius: 4,
          data: this.data,
        }]
      },
      options: gradientChartOptionsConfigurationWithTooltipRed
    };
    this.myChartData = new Chart(this.ctx, config);


    this.canvas = document.getElementById("CountryChart");
    this.ctx  = this.canvas.getContext("2d");
    var gradientStroke = this.ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(29,140,248,0.2)');
    gradientStroke.addColorStop(0.4, 'rgba(29,140,248,0.0)');
    gradientStroke.addColorStop(0, 'rgba(29,140,248,0)'); //blue colors


    var myChart = new Chart(this.ctx, {
      type: 'bar',
      responsive: true,
      legend: {
        display: false
      },
      data: {
        labels: ['USA', 'GER', 'AUS', 'UK', 'RO', 'BR'],
        datasets: [{
          label: "Countries",
          fill: true,
          backgroundColor: gradientStroke,
          hoverBackgroundColor: gradientStroke,
          borderColor: '#1f8ef1',
          borderWidth: 2,
          borderDash: [],
          borderDashOffset: 0.0,
          data: [53, 20, 10, 80, 100, 45],
        }]
      },
      options: gradientBarChartConfiguration
    });
    this.setCandelGraph();

  }
  public updateOptions() {
    this.myChartData.data.datasets[0].data = this.data;
    this.myChartData.update();
  }

  public updateOptions2(char : String) {
    if (char === "btc") {
      this.garde1 = "btc";
      this.selectedCandel = "Bitcoin"
    } else if (char === "bnb") {
      this.garde1 = "bnb";
      this.selectedCandel = "Binance"
    } else if (char === "eth") {
      this.garde1 = "eth";
      this.selectedCandel = "Ethereum"
    }else if (char === "xrp") {
      this.garde1 = "xrp";
      this.selectedCandel = "Xrp"
    }else if (char == "aave") {
      this.garde1 = "aave";
      this.selectedCandel = "AAVE"
    }else if (char == "ada") {
      this.garde1 = "ada";
      this.selectedCandel = "Cardano"
    }else if (char == "bch") {
      this.garde1 = "bch";
      this.selectedCandel = "Bitcoin cash"
    }else if (char == "doge") {
      this.garde1 = "doge";
      this.selectedCandel = "Dogecoin"
    }else if (char == "dot") {
      this.garde1 = "dot";
      this.selectedCandel = "Polkadot"
    }else if (char == "trx") {
      this.garde1 = "trx";
      this.selectedCandel = "Tron"
    }
    this.date = this.data_coins[this.garde1 + "_dates"]
    this.open = this.data_coins[this.garde1][0].map((i: any) => Number(i));
    this.high = this.data_coins[this.garde1][1].map((i: any) => Number(i));
    this.low  = this.data_coins[this.garde1][2].map((i: any) => Number(i));
    this.close= this.data_coins[this.garde1][3].map((i: any) => Number(i));
    this.setCandelGraph();
      
  }

  public updateOptions3(char : String) {
    if (char === "btc") {
      this.garde1 = "btc";
    } else if (char === "bnb") {
      this.garde1 = "bnb";
    } else if (char === "eth") {
      this.garde1 = "eth";
    }else if (char === "xrp") {
      this.garde1 = "xrp";
    }
    this.date = this.data_coins[this.garde1 + "_dates"]
    this.adj_close= this.data_coins[this.garde1][3].map((i: any) => Number(i));
    this.setClosePriceGraph();

  }

  public updateOptions4(char : String) {
    if (char === "btc") {
      this.garde2 = 0;
      this.selectedReturn = "Bitcoin"
      this.return_dates = this.data_coins["btc_dates"]
    } else if (char === "bnb") {
      this.garde2 = 1;
      this.selectedReturn = "Binance"
      this.return_dates = this.data_coins["bnb_dates"]
    } else if (char === "eth") {
      this.garde2 = 2;
      this.selectedReturn = "Ethereum"
      this.return_dates = this.data_coins["eth_dates"]
    }else if (char === "xrp") {
      this.garde2 = 3;
      this.selectedReturn = "XRP"
      this.return_dates = this.data_coins["xrp_dates"]
    }else if (char === "aave") {
      this.garde2 = 4;
      this.selectedReturn = "AAVE"
      this.return_dates = this.data_coins["aave_dates"]
    }else if (char == "ada") {
      this.garde2 = 5;
      this.selectedReturn = "Cardano"
      this.return_dates = this.data_coins["ada_dates"]
    }else if (char == "bch") {
      this.garde2 = 6;
      this.selectedReturn = "Bitcoin cash"
      this.return_dates = this.data_coins["bch_dates"]
    }else if (char == "doge") {
      this.garde2 = 7;
      this.selectedReturn = "Dogecoin"
      this.return_dates = this.data_coins["doge_dates"]
    }else if (char == "dot") {
      this.garde2 = 8;
      this.selectedReturn = "Polkadot"
      this.return_dates = this.data_coins["dot_dates"]
    }else if (char == "trx") {
      this.garde2 = 9;
      this.selectedReturn = "Tron"
      this.return_dates = this.data_coins["trx_dates"]
    }
    this.setReturnGraph();
      
  }

  public updateOptions5(char : String) {
    if (char === "btc") {
      this.garde3 = 0;
      this.selectedHistg = "Bitcoin"
      this.date = this.data_coins["btc_dates"]
    } else if (char === "bnb") {
      this.garde3 = 1;
      this.selectedHistg = "Binance"
      this.date = this.data_coins["bnb_dates"]
    } else if (char === "eth") {
      this.garde3 = 2;
      this.selectedHistg = "Ethereum"
      this.date = this.data_coins["eth_dates"]
    }else if (char === "xrp") {
      this.garde3 = 3;
      this.selectedHistg = "Xrp"
      this.date = this.data_coins["xrp_dates"]
    }else if (char === "aave") {
      this.garde3 = 4;
      this.selectedHistg = "AAVE"
      this.date = this.data_coins["aave_dates"]
    }else if (char == "ada") {
      this.garde3 = 5;
      this.selectedHistg = "Cardano"
      this.date = this.data_coins["ada_dates"]
    }else if (char == "bch") {
      this.garde3 = 6;
      this.selectedHistg = "Bitcoin cash"
      this.date = this.data_coins["bch_dates"]
    }else if (char == "doge") {
      this.garde3 = 7;
      this.selectedHistg = "Dogecoin"
      this.date = this.data_coins["doge_dates"]
    }else if (char == "dot") {
      this.garde3 = 8;
      this.selectedHistg = "Polkadot"
      this.date = this.data_coins["dot_dates"]
    }else if (char == "trx") {
      this.garde3 = 9;
      this.selectedHistg = "Tron"
      this.date = this.data_coins["trx_dates"]
    }
    this.setHistogramegraph()
      
  }
  
  getAllData = () => {
    this.api.getAllData().subscribe(
      (data) => {
        console.log(data)
        this.data_coins = data
        this.date = data[this.garde1 + "_dates"]
        this.open = data[this.garde1][0].map((i: any) => Number(i));
        this.high = data[this.garde1][1].map((i: any) => Number(i));
        this.low = data[this.garde1][2].map((i: any) => Number(i));
        this.close      = data[this.garde1][3].map((i: any) => Number(i));
        //console.log(this.open);
        this.setCandelGraph();
        this.setClosePriceGraph();
        this.updateOptions4("btc");
      },
      (error) => {
        console.log(error)
      }
    )
      
  }

  Returns = () => {
    this.api.Returns().subscribe(
      data => {
        console.log(data)
        this.returns = data.doubles
        this.setReturnGraph()
        this.setHistogramegraph()
      },
      error => {
        console.log(error)
      }
    )
  }

  getCorrelation = () => {
    this.api.Correlation().subscribe(
      data => {
        this.correlation = data.corr
        console.log(this.correlation)
        this.setCorrelationGraph()
      },
      error => {
        console.log(error)
      }
    )
  }

  getVolatilty = () => {
    this.api.Volatilty().subscribe(
      data => {
        console.log(data)
        this.volatilty = data.std
        this.setVolatiltyGraph()
      },
      error => {
        console.log(error)
      }
    )
  }

  setCandelGraph = () => {
  this.candelgraph = {
    
    data: [
      {
        x: this.date, 
        
        close: this.close, 
        
        
        
        high: this.high, 
        
        
        
        line: {color: 'rgba(31,119,180,1)'}, 
        
        low: this.low, 
        
        open: this.open, 
        
        type: 'candlestick', 
        xaxis: 'x', 
        yaxis: 'y'
      }
    ],
    layout: {
      dragmode: 'zoom', 
      margin: {
        r: 10, 

        l: 60
      }, 
      showlegend: false, 
      //paper_bgcolor: 'rgba(0,0,0,0)',
      //plot_bgcolor: 'rgba(0,0,0,0)',
      //font: {color: 'white'},
      xaxis: {
        autorange: true, 
        //domain: [0, 1], 
        //range: ['2021-05-04T00:00:00+00:00', '2022-05-03T00:00:00+00:00'], 
        //rangeslider: {range: ['2021-05-04T00:00:00+00:00', '2022-05-03T00:00:00+00:00'],
        //bgcolor: "rgb(233,233,233)"
      //}, 
        //title: 'Date', 
        type: 'date'
      }, 
      yaxis: {
        autorange: true, 
        //domain: [0, 1], 
        //range: [114.609999778, 137.410004222], 
        type: 'linear'
      }
    }
  };

 }

  setClosePriceGraph = () => {
  this.closeprice = {

    data: [
      {
        type: "scatter",
        mode: "lines",
        x: this.date,
        y: this.adj_close,
        line: {color: '#17BECF'}
      },

    ],
    layout: {
      xaxis: {
        autorange: true, 
        //domain: [0, 1], 
        //range: ['2021-05-04T00:00:00+00:00', '2022-05-03T00:00:00+00:00'], 
        //rangeslider: {range: ['2021-05-04T00:00:00+00:00', '2022-05-03T00:00:00+00:00'],
        //bgcolor: "rgb(233,233,233)"
      //}, 
        title: 'Date', 
        type: 'date'
      }, 
      yaxis: {
        autorange: true
        //domain: [0, 1], 
        //range: [114.609999778, 137.410004222], 
      }
    }
  };
 }

  setReturnGraph = () => {
  this.returnsgraph = {
  
    data: [
      {
        type: "scatter3D",
        mode: "lines",
        x: this.return_dates,
        y: this.returns[this.garde2],
      },

    ],
    layout: {
        //paper_bgcolor: 'rgba(0,0,0,0)',
        //plot_bgcolor: 'rgb(233,233,233)',
        //font: {color: 'white'},
        colorbar: true,
        xaxis: {
          autorange: true,
          domain: [0, 1],
          range: ['2021-05-04T00:00:00+00:00', '2022-05-03T00:00:00+00:00'],
          rangeselector: {buttons: [
              {
                count: 1,
                label: '1m',
                step: 'month',
                stepmode: 'backward'
              },
              {
                count: 6,
                label: '6m',
                step: 'month',
                stepmode: 'backward'
              },
              {step: 'all'}
            ]},
          rangeslider: {range: ['2021-05-04T00:00:00+00:00', '2022-05-03T00:00:00+00:00']},
          type: 'date'
        },
        yaxis: {
          autorange: true,
          domain: [0, 1],
          range: [114.609999778, 138.870004167],
          type: 'linear'
        }
    }
  };
}

  setHistogramegraph = () => {
  this.histograme = {

    data: [
      {

        x: this.returns[this.garde3], 
        type: "histogram", 
        opacity: 0.5,
        marker: {
          color: "rgba(255, 100, 102, 0.7)", 
          line: {
          color:  "rgba(255, 100, 102, 1)", 
          width: 1
          } 
       }, 
      }

    ]

    };
}

  setCorrelationGraph = () => {
  this.correlationgraph = {

    data: [
      {
        z: this.correlation,
        x: ['Bitcoin', 'Binance', 'Ethereum', 'XRP', 'AAVE', "Cardano", "Bitcoin Cash", "Dogecoin", "Polkadot", "Tron"],
        y: ['Bitcoin', 'Binance', 'Ethereum', 'XRP', 'AAVE', "Cardano", "Bitcoin Cash", "Dogecoin", "Polkadot", "Tron"],
        type: 'heatmap',
        
      },

    ],
    layout: {
        annotations : [],
        xaxis: {
          ticks: '',
          side: 'top'
        },
        
    }
    
  };

  for ( let i = 0; i < 10; i++ ) {
    for ( let j = 0; j < 10; j++ ) {
      var currentValue = this.correlation[i][j];
      if (currentValue != 0.0) {
        var textColor = 'white';
      }else{
        var textColor = 'black';
      }
      var result = {
        xref: 'x1',
        yref: 'y1',
        x: ['Bitcoin', 'Binance', 'Ethereum', 'XRP', 'AAVE', "Cardano", "Bitcoin Cash", "Dogecoin", "Polkadot", "Tron"][j],
        y: ['Bitcoin', 'Binance', 'Ethereum', 'XRP', 'AAVE', "Cardano", "Bitcoin Cash", "Dogecoin", "Polkadot", "Tron"][i],
        text: Math.round(this.correlation[i][j] * 100 + Number.EPSILON ) / 100,
        font: {
          family: 'Arial',
          size: 12,
          color: textColor
        },
        showarrow: false,

      };
      this.correlationgraph.layout.annotations.push(result);
    }
};
}

  setVolatiltyGraph = () => {
  this.volatiltygraph = {

    data: [
      {
        y: ['Bitcoin', 'Binance', 'Ethereum', 'XRP', 'AAVE', "Cardano", "Bitcoin Cash", "Dogecoin", "Polkadot", "Tron"],
        x: this.volatilty,
        type: 'bar',
        text: this.volatilty.map(String),
        orientation: 'h',
        textposition: 'auto',
        hoverinfo: 'none',
        marker: {
          color: 'rgb(158,202,225)',
          opacity: 0.6,
          line: {
            color: 'rgb(8,48,107)',
            width: 1.5
          }
        }
      }

    ],
    layout: {
      barmode: 'stack'
      }
    };
}

 showNotification(from, align){

  const color = Math.floor((Math.random() * 5) + 1);


    this.toastr.error('<span class="tim-icons icon-bell-55" [data-notify]="icon"></span> Welcome to <b>Data Visualisation Dashboard</b> for Cryptocurrency data analysis end of module project. Supervised by : Pr.M. EL AACHAK Lotfi', '', {
       disableTimeOut: true,
       enableHtml: true,
       closeButton: true,
       toastClass: "alert alert-danger alert-with-icon",
       positionClass: 'toast-' + from + '-' +  align
     });

}

}
