import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/architecture/services/auth.service';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';
import { Location } from '@angular/common';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-docsearch',
  templateUrl: './docsearch.component.html',
  styleUrls: ['./docsearch.component.css'],
})
export class DocsearchComponent implements OnInit {
  allDoctors: any[] = []; // Store all doctors
  currentUserRole: string = '';
  searchQuery: string = '';
  searchResults: any[] = [];
  selectedCity: string = '';
  afterSearchData: any[] = [];
  searchSuggestions: string[] = [
    'Dentist',
    'Gynecologist',
    'General Physician',
    'Dermatologist',
    'Ear-nose-throat Specialist',
    'Homoeopath',
    'Ayurveda',
  ];
  cities: string[] = [
    'Karachi',
    'Lahore',
    'Islamabad',
    'Rawalpindi',
    'Faisalabad',
    'Multan',
    'Hyderabad',
    'Quetta',
    'Peshawar',
    'Gujranwala',
    'Sialkot',
    'Abbottabad',
    'Bahawalpur',
    'Sargodha',
    'Sukkur',
    'Larkana',
    'Nawabshah',
    'Mirpur Khas',
    'Rahim Yar Khan',
    'Sahiwal',
    'Okara',
    'Wah Cantonment',
    'Dera Ghazi Khan',
    'Mingora',
    'Kamoke',
    'Shekhupura',
    'Mardan',
    'Kasur',
    'Gujrat',
    'Chiniot',
    'Jhang',
    'Sadiqabad',
    'Sheikhupura',
    'Attock',
    'Jhelum',
    'Jacobabad',
    'Khanewal',
    'Muzaffargarh',
    'Khanpur',
  ];

  constructor(
    private patientService: PatientService,
    private router: Router,
    private authService: AuthService,
    private location: Location,
    private http: HttpClient
  ) {}

  ngOnInit(): void {
    this.getCurrentUserRole();
    this.loadAllDoctors();
  }

  loadAllDoctors() {
    this.patientService.getAllDoctors().subscribe({
      next: (response: any) => {
        this.allDoctors = response.results;
        this.searchResults = this.allDoctors;
      },
      error: (error) => {
        console.error('Error fetching doctors:', error);
      },
      complete: () => {
        console.log('Doctor loading complete');
      },
    });
  }
  getCurrentUserRole() {
    this.authService.user().subscribe((user: any) => {
      this.currentUserRole = user.role;
    });
  }

  searchDoctors() {
    let query = this.searchQuery.toLowerCase();
    let city = this.selectedCity;

    this.searchResults = this.allDoctors.filter((doctor) => {
      // Match doctor name and city with search query and selected city
      // Adjust the condition based on your data structure
      let matchesQuery = doctor.full_name.toLowerCase().includes(query);
      let matchesCity = city ? doctor.city === city : true;
      return matchesQuery && matchesCity;
    });
  }

  doctorsSearched() {
    this.patientService
      .afterDoctorsSearched(this.searchQuery, this.selectedCity)
      .subscribe((response: any) => {
        this.afterSearchData = response.results;
      });
  }

  goBack(): void {
    this.location.back();
  }

  onBookAppointment(docId: any) {
    this.router.navigate([
      '/dashboard/patient/appointment/booking',
      { doctorId: docId },
    ]);
  }
}
