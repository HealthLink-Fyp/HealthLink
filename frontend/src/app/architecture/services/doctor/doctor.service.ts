import { HttpClient } from '@angular/common/http';
import { EventEmitter, Injectable } from '@angular/core';
import { withCache } from '@ngneat/cashew';
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

  
  getChatHistory(body: any) {
    return this.http.post(`${environment.api}/chat/`, body);
  }

  sendNotes(body:any)
  {
    return this.http.post(`${environment.api}/records/`, body);
  }

  getbookedAppointments()
  {
    return this.http.get(`${environment.api}/appointment/`)
  }

  delAppointment(pkAppointment: any)
  {
    return this.http.delete(`${environment.api}/appointment/${pkAppointment}/`);
  }

  updateDoctorProfile(body:any)
  {
    return this.http.put(`${environment.api}/auth/profile/`,body);
  }

  deleteDoctor()
  {
    return this.http.delete(`${environment.api}/auth/user/`);
  }

  delDocForm()
  {
    return this.http.delete(`${environment.api}/auth/profile/`);
  }

  
}
