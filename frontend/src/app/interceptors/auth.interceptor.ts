
import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpErrorResponse
} from '@angular/common/http';
import { Observable, catchError, switchMap, throwError } from 'rxjs';
import { AuthService } from '../services/auth.service';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  refresh=false;
  

  constructor(private authService:AuthService) {}

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const clonedReq = req.clone({
      setHeaders: {
        Authorization: `Bearer ${this.authService.accessToken}`
      }
    });
  
    return next.handle(clonedReq).pipe(
      catchError((err: HttpErrorResponse) => {
        if (err.status === 401 && !this.refresh) {
          this.refresh=true;

          return this.authService.refresh().pipe(
            switchMap((res: any) => {
              this.authService.accessToken = res.token;
              return next.handle(req.clone({
                setHeaders: {
                  Authorization: `Bearer ${this.authService.accessToken}`
                }
              }));
            })
          );
        } 
          this.refresh=false;
          return throwError(()=>err);
        
      })
    );
  }
  
}
