import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/architecture/services/auth.service';
import { DoctorService } from 'src/app/architecture/services/doctor/doctor.service';

@Component({
  selector: 'app-dsidenav',
  templateUrl: './dsidenav.component.html',
  styleUrls: ['./dsidenav.component.css'],
})
export class DsidenavComponent implements OnInit {
  doctorData: any = {};

  constructor(
    private doctorService: DoctorService,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    this.doctorService.getDoctor().subscribe((res: any) => {
      this.doctorData = res;
      // console.log("coming from dashboard", this.doctorData);
    });
  }

  logout() {
    this.authService.logout().subscribe(() => {
      this.authService.accessToken = '';
      AuthService.authEmitter.emit(false);
    });
  }
}
