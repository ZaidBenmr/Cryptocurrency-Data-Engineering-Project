import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../api.service';

@Component({
  selector: 'app-predictions',
  templateUrl: './predictions.component.html',
  providers : [ApiService]
})
export class PredictionsComponent implements OnInit {


  inputString : string = "btc"
  selectedCrypto : string = "Bitcoin"
  predictionResult : any
  predictionDates : any
  predicitonsgraph : any

  dates : any
  close : any

  constructor(private api:  ApiService) { 
    this.Predictions();
  }

  ngOnInit(): void {
  }

  public updateOptions(char : string) {

    this.inputString = char
    if (char === "btc") {
      this.selectedCrypto = "Bitcoin"
    } else if (char === "bnb") {
      this.selectedCrypto = "Binance"
    } else if (char === "eth") {
      this.selectedCrypto = "Ethereum"
    }else if (char === "xrp") {
      this.selectedCrypto = "Xrp"
    }else if (char == "aave") {
      this.selectedCrypto = "AAVE"
    }else if (char == "ada") {
      this.selectedCrypto = "Cardano"
    }else if (char == "bch") {
      this.selectedCrypto = "Bitcoin cash"
    }else if (char == "doge") {
      this.selectedCrypto = "Dogecoin"
    }else if (char == "dot") {
      this.selectedCrypto = "Polkadot"
    }else if (char == "trx") {
      this.selectedCrypto = "Tron"
    }
    this.Predictions();
      
  }
  
  Predictions = () => {
    this.api.Predictions(this.inputString).subscribe(
      data => {
        console.log(data)
        this.predictionDates  = data.dates
        this.predictionResult = data.values
        this.getAllData()
      },
      error => {
        console.log(error)
      }
    )
  }

  getAllData = () => {
    this.api.getAllData().subscribe(
      (data) => {
        console.log(data)
        this.dates = data[this.inputString + "_dates"]
        this.close      = data[this.inputString][3].map((i: any) => Number(i));
        this.setPredictionsGraph();
      },
      (error) => {
        console.log(error)
      }
    )
  }



 setPredictionsGraph = () => {
  this.predicitonsgraph = {

    data: [
      {
        type: "scatter",
        mode: "lines",
        name: 'Historical data',
        x: this.dates,
        y: this.close,
        line: {color: '#17BECF'}
      },
      {
        type: "scatter",
        mode: "lines",
        name: 'Predictions',
        x: this.predictionDates,
        y: this.predictionResult,
        line: {color: '#7F7F7F'}
      },

    ],
    layout: {
      plot_bgcolor: 'rgb(245, 245, 255)',
      paper_bgcolor: 'white',
      xaxis: {
        gridcolor: 'rgb(255, 255, 255)',
      },
      yaxis: {
        gridcolor: 'rgb(255, 255, 255)',
      },
    }
  };
 }
}
