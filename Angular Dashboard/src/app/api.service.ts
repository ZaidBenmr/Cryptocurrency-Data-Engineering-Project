import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  // Just For test Now
  BASE_URL = "http://127.0.0.1:8000/"
  BASE_URL2 = "http://localhost:9200/"
  HTTP_HEADERS = new HttpHeaders({'Content-Type' : 'application/json'})

  
  getAllData() : Observable<any> {
    return this.http.get(this.BASE_URL + "bitcoin/", 
    {headers : this.HTTP_HEADERS})
  }

  Returns() : Observable<any> {
    return this.http.get(this.BASE_URL + "returns/", 
    {headers : this.HTTP_HEADERS})
  }

  Volatilty() : Observable<any> {
    return this.http.get(this.BASE_URL + "volatilty/", 
    {headers : this.HTTP_HEADERS})
  }
  
  Correlation() : Observable<any> {
    return this.http.get(this.BASE_URL + "correlation/", 
    {headers : this.HTTP_HEADERS})
  }

  Predictions(id: string) : Observable<any> {
    return this.http.get(`${this.BASE_URL}predictions/${id}/`,
    {headers:this.HTTP_HEADERS})
  }

  CryptoBalance() : Observable<any> {

    const query = {
      size: 100,
      sort: [{ datetime: 'desc' }]
    };
    // Convert the query object to a string
    const queryBody = JSON.stringify(query);

    return this.http.post(this.BASE_URL2 + 'crypto_balance/_search', queryBody, {
      headers: this.HTTP_HEADERS
    });
    
  }

  
}