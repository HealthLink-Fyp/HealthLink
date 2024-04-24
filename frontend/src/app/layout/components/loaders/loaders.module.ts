import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LoadersRoutingModule } from './loaders-routing.module';
import { LoadersComponent } from './loaders.component';

import { NgxSkeletonLoaderModule } from 'ngx-skeleton-loader';

@NgModule({
  declarations: [
    LoadersComponent
  ],
  imports: [
    CommonModule,
    LoadersRoutingModule,
    NgxSkeletonLoaderModule,
  ]
})
export class LoadersModule { }
