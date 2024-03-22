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
    ["general_practice", "General Practice"],
    ["child_care", "Child Care"],
    ["women_health", "Women Health"],
    ["bone_joint_care", "Bone & Joint Care"],
    ["heart_care", "Heart Care"],
    ["skin_care", "Skin Care"],
    ["eye_care", "Eye Care"],
    ["dental_care", "Dental Care"],
    ["mental_health", "Mental Health"],
    ["brain_nervous_system_care", "Brain & Nervous System Care"],
    ["digestive_health", "Digestive Health"],
    ["urinary_tract_health", "Urinary Tract Health"],
    ["cancer_care", "Cancer Care"],
    ["ear_nose_throat_care", "Ear, Nose & Throat Care"],
    ["hormone_health", "Hormone Health"],
    ["joint_health", "Joint Health"],
    ["allergy_immune_system_care", "Allergy & Immune System Care"],
    ["lung_respiratory_health", "Lung & Respiratory Health"],
    ["kidney_health", "Kidney Health"],
    ["physical_therapy", "Physical Therapy"],
  ];

  QUALIFICATION_CHOICES: [string, string][] = [
    ['mbbs', 'MBBS'],
    ['bds', 'BDS'],
    ['md', 'MD'],
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
}
