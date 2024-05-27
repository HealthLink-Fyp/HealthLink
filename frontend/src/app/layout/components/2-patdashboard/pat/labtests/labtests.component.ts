import { Component } from '@angular/core';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';
import { Location } from '@angular/common';

@Component({
  selector: 'app-labtests',
  templateUrl: './labtests.component.html',
  styleUrls: ['./labtests.component.css']
})
export class LabtestsComponent {

  tests:any = [];
totalRecords = 0;
filteredTests:any = [];
searchTerm = '';

constructor(private labService:PatientService, private location: Location){}

goBack(): void {
  this.location.back();
}

ngOnInit(): void {
  this.getTests(0);
}

getTests(offset: number) {
  this.labService.getTests(10, offset).subscribe((response: any) => {
    this.tests = response.results;
    this.totalRecords = response.count;
  });
}

onPageChange(event: any) {
  this.getTests(event.pageIndex * event.pageSize);
}

selectedCity:string='';

cities:string[]=[
  'Karachi', 'Lahore', 'Islamabad', 'Rawalpindi', 'Faisalabad', 'Multan', 'Hyderabad', 'Quetta', 'Peshawar', 'Gujranwala', 'Sialkot', 'Abbottabad', 'Bahawalpur', 'Sargodha', 'Sukkur', 'Larkana', 'Nawabshah', 'Mirpur Khas', 'Rahim Yar Khan', 'Sahiwal', 'Okara', 'Wah Cantonment', 'Dera Ghazi Khan', 'Mingora', 'Kamoke', 'Shekhupura', 'Mardan', 'Kasur', 'Gujrat', 'Chiniot', 'Jhang', 'Sadiqabad', 'Sheikhupura', 'Attock', 'Jhelum', 'Jacobabad', 'Khanewal', 'Muzaffargarh', 'Khanpur'
  ]

  search() {
    this.filteredTests = this.tests.filter((test:any) => test.name.toLowerCase().includes(this.searchTerm.toLowerCase()));
  }

searchSuggestions: string[] = ['One', 'Two', 'Three'];


}
