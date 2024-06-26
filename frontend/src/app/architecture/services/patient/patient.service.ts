import { HttpClient } from '@angular/common/http';
import { EventEmitter, Injectable } from '@angular/core';
import { withCache } from '@ngneat/cashew';
import { environment } from 'src/environment/environment';

@Injectable({
  providedIn: 'root',
})
export class PatientService {
  static authEmitter = new EventEmitter<boolean>();

  constructor(private http: HttpClient) {}

  register(body: any) {
    return this.http.post(`${environment.api}/auth/profile/`, body);
  }

  getPatient() {
    // console.log("hi i am getting patient for u (service)");
    return this.http.get(`${environment.api}/auth/profile/`, {
      context: withCache(),
    });
  }

  uploadFile(formData: FormData) {
    return this.http.post(`${environment.api}/records/`, formData);
  }

  getRecords() {
    return this.http.get(`${environment.api}/records/`);
  }

  getChatHistory(body: any) {
    return this.http.post(`${environment.api}/chat/`, body);
  }

  updatePatientProfile(body: any) {
    return this.http.put(`${environment.api}/auth/profile/`, body);
  }

  deletePatient() {
    return this.http.delete(`${environment.api}/auth/user/`);
  }

  getAllDoctors() {
    return this.http.get(`${environment.api}/search/doctors/`);
  }

  delPatForm() {
    return this.http.delete(`${environment.api}/auth/profile/`);
  }

  updateAppointment(body: any, pkAppointment: any) {
    return this.http.put(
      `${environment.api}/appointment/${pkAppointment}/`,
      body
    );
  }

  delAppointment(pkAppointment: any) {
    return this.http.delete(`${environment.api}/appointment/${pkAppointment}/`);
  }

  searchDoctors(query: string) {
    return this.http.get(
      `${environment.api}/search/doctors/autocomplete/?search=${query}`
    );
  }

  allDoctors() {
    return this.http.get(`${environment.api}/search/doctors/`);
  }

  afterDoctorsSearched(query: string, city: string) {
    const params = { search: query, city: city };
    return this.http.get(`${environment.api}/search/doctors/`, {
      params: params,
    });
  }

  getDoctorProfile(userId: number) {
    return this.http.get(`${environment.api}/doctors/${userId}/`);
  }

  makeAppointment(body: any) {
    return this.http.post(`${environment.api}/appointment/`, body);
  }

  getbookedAppointments() {
    return this.http.get(`${environment.api}/appointment/`);
  }

  getbookedAppointment(body: any) {
    return this.http.get(`${environment.api}/appointment/`, body);
  }

  getMedicines(limit: number, offset: number) {
    return this.http.get(`${environment.api}/medicines/`, {
      params: {
        limit,
        offset,
      },
    });
  }

  getTests(limit: number, offset: number) {
    return this.http.get(`${environment.api}/tests/`, {
      params: {
        limit: limit,
        offset: offset,
      },
    });
  }
}
