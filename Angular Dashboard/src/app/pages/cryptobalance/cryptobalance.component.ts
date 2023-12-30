import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../api.service';

@Component({
  selector: 'app-cryptobalance',
  templateUrl: './cryptobalance.component.html',
  providers : [ApiService]
})
export class CryptobalanceComponent implements OnInit {

  cryptoBalanceData : any

  constructor(private api:  ApiService) { 
    this.getCryptoBalance();
  }

  ngOnInit(): void {
  }

  getCryptoBalance = () => {
    this.api.CryptoBalance().subscribe(
      data => {
        this.cryptoBalanceData = data.hits.hits;
        console.log(data.hits.hits) 
        
      },
      error => {
        console.log(error)
      }
    )
  }
}
