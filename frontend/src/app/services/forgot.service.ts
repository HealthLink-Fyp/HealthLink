import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environment/environment';

@Injectable({
  providedIn: 'root',
})
export class ForgotService {
  constructor(private http: HttpClient) {}

  forgot(body: any) {
    return this.http.post(`${environment.api}/auth/forget/`, body);
  }

  reset(body: any) {
    return this.http.post(`${environment.api}/auth/reset/`, body);
  }
}
