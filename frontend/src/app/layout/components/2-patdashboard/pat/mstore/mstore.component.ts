import { Component, OnInit } from '@angular/core';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';

@Component({
  selector: 'app-mstore',
  templateUrl: './mstore.component.html',
  styleUrls: ['./mstore.component.css']
})
export class MstoreComponent implements OnInit {

  medicines:any = [];
  totalResults = 0;

  constructor(private medicineService:PatientService){}

  ngOnInit(): void {
       this.getMedicines(0);
    
  }

  getMedicines(offset: number) {
    this.medicineService.getMedicines(10, offset).subscribe((response: any) => {
      this.medicines = response.results;
      this.totalResults = response.count;
    });
  }

  onPageChange(event: any) {
    this.getMedicines(event.pageIndex * event.pageSize);
  }

 

  selectedCity:string='';

  cities:string[]=[
    'Karachi', 'Lahore', 'Islamabad', 'Rawalpindi', 'Faisalabad', 'Multan', 'Hyderabad', 'Quetta', 'Peshawar', 'Gujranwala', 'Sialkot', 'Abbottabad', 'Bahawalpur', 'Sargodha', 'Sukkur', 'Larkana', 'Nawabshah', 'Mirpur Khas', 'Rahim Yar Khan', 'Sahiwal', 'Okara', 'Wah Cantonment', 'Dera Ghazi Khan', 'Mingora', 'Kamoke', 'Shekhupura', 'Mardan', 'Kasur', 'Gujrat', 'Chiniot', 'Jhang', 'Sadiqabad', 'Sheikhupura', 'Attock', 'Jhelum', 'Jacobabad', 'Khanewal', 'Muzaffargarh', 'Khanpur'
    ]

  search()
  {
    
  }

  searchSuggestions: string[] = ['One', 'Two', 'Three'];


}
