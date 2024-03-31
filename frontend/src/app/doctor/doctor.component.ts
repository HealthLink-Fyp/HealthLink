import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, FormArray, FormControl } from '@angular/forms';
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
  message = '';
  authenticated = false;

  SPECIALIZATION_CHOICES: [string, string][] = [
    ['general_practice', 'General Practice'],
    ['child_care', 'Child Care'],
    ['women_health', 'Women Health'],
    ['bone_joint_care', 'Bone & Joint Care'],
    ['heart_care', 'Heart Care'],
    ['skin_care', 'Skin Care'],
    ['eye_care', 'Eye Care'],
    ['dental_care', 'Dental Care'],
    ['mental_health', 'Mental Health'],
    ['brain_nervous_system_care', 'Brain & Nervous System Care'],
    ['digestive_health', 'Digestive Health'],
    ['urinary_tract_health', 'Urinary Tract Health'],
    ['cancer_care', 'Cancer Care'],
    ['ear_nose_throat_care', 'Ear, Nose & Throat Care'],
    ['hormone_health', 'Hormone Health'],
    ['joint_health', 'Joint Health'],
    ['allergy_immune_system_care', 'Allergy & Immune System Care'],
    ['lung_respiratory_health', 'Lung & Respiratory Health'],
    ['kidney_health', 'Kidney Health'],
    ['physical_therapy', 'Physical Therapy'],
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
    'Saturday',
    'Sunday',
  ];

  constructor(
    private formBuilder: FormBuilder,
    private doctorService: DoctorService,
    private authService: AuthService,
    private router: Router
  ) {}

  ngOnInit(): void {
    AuthService.authEmitter.subscribe((authenticated) => {
      this.authenticated = authenticated;
    });

    this.form = this.formBuilder.group({
      specialization: '',
      qualification: '',
      experience_years: '',
      city: '',
      start_time: '',
      end_time: '',
      available_days: new FormArray([]),
      consultation_fees: '',
      summary: '',
      wait_time: '',
    });
  }

  onCheckboxChange(i: number, e: any) {
    const availableDays: FormArray = this.form.get(
      'available_days'
    ) as FormArray;

    if (e.target.checked) {
      this.addDay(e.target.value, availableDays);
    } else {
      this.removeDay(e.target.value, availableDays);
    }
  }

  addDay(day: string, availableDays: FormArray) {
    availableDays.push(new FormControl(day.toLowerCase()));
  }

  removeDay(day: string, availableDays: FormArray) {
    let index = availableDays.controls.findIndex((x) => x.value === day);
    availableDays.removeAt(index);
  }

  submit() {
    let doctor_data = this.prepareDoctorData();
    this.doctorService
      .register(doctor_data)
      .subscribe((res) => console.log(res));
    this.router.navigate(['/dboard']);
  }

  prepareDoctorData() {
    let formValue = this.form.getRawValue();

    let availability_data = {
      days: formValue.available_days,
      start: formValue.start_time,
      end: formValue.end_time,
    };

    let doctor_data = {
      specialization: formValue.specialization,
      qualification: formValue.qualification,
      experience_years: formValue.experience_years,
      city: formValue.city,
      consultation_fees: formValue.consultation_fees,
      summary: formValue.summary,
      wait_time: formValue.wait_time,
      availability_data: availability_data,
    };

    return doctor_data;
  }

  Done() {
    this.router.navigate(['/dboard']);
  }
}
