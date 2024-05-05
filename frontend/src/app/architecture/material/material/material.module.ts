import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {MatCardModule} from '@angular/material/card';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatDividerModule} from '@angular/material/divider';
import { MatListModule } from '@angular/material/list';
import { MatSidenavModule } from '@angular/material/sidenav';
import {MatSelectModule} from '@angular/material/select';
import {MatFormFieldModule} from '@angular/material/form-field';
import {FormsModule} from '@angular/forms';
import {MatInputModule} from '@angular/material/input';
import {MatAutocompleteModule} from '@angular/material/autocomplete';
import { MatRadioModule } from '@angular/material/radio';
import {MatTabsModule} from '@angular/material/tabs';
import {MatStepperModule} from '@angular/material/stepper';
import { MatSnackBarModule} from '@angular/material/snack-bar';
import {MatSlideToggleModule} from '@angular/material/slide-toggle';

import {ClipboardModule} from '@angular/cdk/clipboard';

import {MatDialogModule} from '@angular/material/dialog';

import { ReactiveFormsModule } from '@angular/forms';

import {MatCheckboxModule} from '@angular/material/checkbox';

import {MatPaginatorModule} from '@angular/material/paginator';




const AllMaterialModules=[MatCardModule,MatIconModule,MatButtonModule,MatToolbarModule,
                          MatDividerModule,MatListModule,MatSidenavModule,MatSelectModule,MatFormFieldModule,FormsModule,MatInputModule,
                        MatAutocompleteModule,MatRadioModule,MatTabsModule,MatStepperModule,
                      MatSnackBarModule,MatSlideToggleModule,ClipboardModule,MatDialogModule,ReactiveFormsModule,MatCheckboxModule,
                      MatPaginatorModule,

     
                      ];

@NgModule({
  imports: [AllMaterialModules,

  ],
  exports: [AllMaterialModules],
})
export class MaterialModule {}
