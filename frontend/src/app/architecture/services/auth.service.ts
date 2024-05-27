import { environment } from '../../../environment/environment';
import { HttpClient } from '@angular/common/http';
import { EventEmitter, Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  static authEmitter = new EventEmitter<boolean>();

  accessToken = '';

  constructor(private http: HttpClient) {}

  register(body: any) {
    return this.http.post(`${environment.api}/auth/register/`, body);
  }

  login(body: any) {
    return this.http.post(`${environment.api}/auth/login/`, body, {
      withCredentials: true,
    });
  }

  user() {
    return this.http.get(`${environment.api}/auth/user/`);
  }

  updateUser(body:any)
  {
    return this.http.put(`${environment.api}/auth/user/`,body);
  }

  refresh() {
    return this.http.post(
      `${environment.api}/auth/refresh/`,
      {},
      { withCredentials: true },
    );
  }

  logout() {
    return this.http.post(
      `${environment.api}/auth/logout/`,
      {},
      { withCredentials: true },
    );
  }
}



// import { Injectable } from '@angular/core';
// import { HttpClient } from '@angular/common/http';
// import { EventEmitter} from '@angular/core';
// import { Observable } from 'rxjs';
// import { environment } from '../../../environment/environment';

// @Injectable({
//   providedIn: 'root'
// })
// export class AuthService {
//   static authEmitter = new EventEmitter<boolean>();
//   accessToken:any = '';

//   constructor(private http: HttpClient) {
//     // Retrieve token from local storage
//     this.accessToken = localStorage.getItem('token');
//   }

//   register(body: any): Observable<any> {
//     return this.http.post(`${environment.api}/auth/register/`, body);
//   }

//   login(body: any): Observable<any> {
//     return this.http.post(`${environment.api}/auth/login/`, body, { withCredentials: true })
//       .subscribe((res: any) => {
//         // Store token in local storage
//         localStorage.setItem('token', res.access_token);
//         this.accessToken = res.access_token;
//       });
//   }

//   user(): Observable<any> {
//     return this.http.get(`${environment.api}/auth/user/`);
//   }

//   updateUser(body: any): Observable<any> {
//     return this.http.put(`${environment.api}/auth/user/`, body);
//   }

//   refresh(): Observable<any> {
//     return this.http.post(`${environment.api}/auth/refresh/`, {}, { withCredentials: true })
//       .subscribe((res: any) => {
//         // Update token in local storage
//         localStorage.setItem('token', res.access_token);
//         this.accessToken = res.access_token;
//       });
//   }

//   logout(): Observable<any> {
//     return this.http.post(`${environment.api}/auth/logout/`, {}, { withCredentials: true });
//   }
// }