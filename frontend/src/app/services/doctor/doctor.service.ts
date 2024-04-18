import { HttpClient } from '@angular/common/http';
import { EventEmitter, Injectable } from '@angular/core';
import { environment } from 'src/environment/environment';

@Injectable({
  providedIn: 'root',
})
export class DoctorService {
  static authEmitter = new EventEmitter<boolean>();

  constructor(private http: HttpClient) {}

  register(body: any) {
    return this.http.post(`${environment.api}/auth/profile/`, body);
  }

  getDoctor() {
    return this.http.get(`${environment.api}/auth/profile/`);
  }

  
}
