import { HttpClient } from '@angular/common/http';
import { EventEmitter, Injectable } from '@angular/core';
import { environment } from 'src/environment/environment';

@Injectable({
  providedIn: 'root',
})
export class PatientService {
  static authEmitter = new EventEmitter<boolean>();

  constructor(private http: HttpClient) {}

  register(body: any) {
    return this.http.post(`${environment.api}/auth/api/profile/`, body);
  }

  getPatient() {
    return this.http.get(`${environment.api}/auth/profile/`);
  }


  searchDoctors(query: string) {
    return this.http.get(
      `${environment.api}/search/doctors/autocomplete/?search=${query}`,
    );
  }

  afterDoctorsSearched(query: string, city: string) {
    const params = { search: query, city: city };
    return this.http.get(`${environment.api}/search/doctors/`, { params: params });
  }
  
  viewDoctor() {
    return this.http.get(`${environment.api}/auth/profile/`);
  }

  
}
