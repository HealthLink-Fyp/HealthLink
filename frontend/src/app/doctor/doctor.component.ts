import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { DoctorService } from '../services/doctor/doctor.service';

@Component({
  selector: 'app-doctor',
  templateUrl: './doctor.component.html',
  styleUrls: ['./doctor.component.css'],
})
export class DoctorComponent implements OnInit {
  form!: FormGroup;

  SPECIALIZATION_CHOICES: [string, string][] = [
    ['cardiologist', 'Cardiologist'],
    ['dentist', 'Dentist'],
    ['dermatologist', 'Dermatologist'],
    ['endocrinologist', 'Endocrinologist'],
    ['gastroenterologist', 'Gastroenterologist'],
    ['gynecologist', 'Gynecologist'],
    ['hematologist', 'Hematologist'],
    ['internist', 'Internist'],
    ['nephrologist', 'Nephrologist'],
    ['neurologist', 'Neurologist'],
    ['neurosurgeon', 'Neurosurgeon'],
    ['obstetrician', 'Obstetrician'],
    ['oncologist', 'Oncologist'],
    ['ophthalmologist', 'Ophthalmologist'],
    ['orthopedic surgeon', 'Orthopedic Surgeon'],
    ['otolaryngologist', 'Otolaryngologist'],
    ['pathologist', 'Pathologist'],
    ['pediatrician', 'Pediatrician'],
    ['physiatrist', 'Physiatrist'],
    ['podiatrist', 'Podiatrist'],
    ['psychiatrist', 'Psychiatrist'],
    ['pulmonologist', 'Pulmonologist'],
    ['radiologist', 'Radiologist'],
    ['rheumatologist', 'Rheumatologist'],
    ['surgeon', 'Surgeon'],
    ['urologist', 'Urologist'],
    ['other', 'Other'],
  ];

  QUALIFICATION_CHOICES: [string, string][] = [
    ['mbbs', 'MBBS'],
    ['bds', 'BDS'],
    ['md', 'MD'],
    ['ms', 'MS'],
    ['dm', 'DM'],
    ['mch', 'MCH'],
    ['phd', 'PHD'],
    ['other', 'Other'],
  ];

  availableDays: string[] = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
  ];

  message = '';

  constructor(
    private formBuilder: FormBuilder,
    private doctorService: DoctorService,
    private authService: AuthService,
    private router:Router
  ) {}

  authenticated = false;

  ngOnInit(): void {
    AuthService.authEmitter.subscribe((authenticated) => {
      this.authenticated = authenticated;
    });

    this.form = this.formBuilder.group({
      specialization: '',

      qualification: '',

      experience_years: '',

      city: '',

      available_timings: '',

      available_days: '',

      consultation_fees: '',

      summary: '',

      wait_time: '',
    });
  }

  submit() {
    this.doctorService
      .register(this.form.getRawValue())
      .subscribe((res) => console.log(res));
      this.router.navigate(['/dboard']);
  }

  Done()
  {
    this.router.navigate(['/dboard']);
  }
}
