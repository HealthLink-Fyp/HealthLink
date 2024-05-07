import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DashboardsRoutingModule } from './dashboards-routing.module';
import { DashboardsComponent } from './dashboards.component';
import { DocComponent } from './doc/doc.component';


import { DsidenavComponent } from './doc/dsidenav/dsidenav.component';



import { MaterialModule } from 'src/app/architecture/material/material/material.module';





import { DformComponent } from './doc/dform/dform.component';

import { DtabsComponent } from './doc/dtabs/dtabs.component';
import { VideocallComponent } from './videocall/videocall.component';
import { TranscriptionComponent } from './videocall/transcription/transcription.component';
import { DialogComponent } from './videocall/dialog/dialog.component';
import { DappointmentComponent } from './doc/dappointment/dappointment.component';
import { AboutComponent } from './doc/about/about.component';
import { ChatComponent } from './chat/chat.component';
import { TodoComponent } from './doc/todo/todo.component';
import { NgxEchartsModule } from 'ngx-echarts';
import { NgxSkeletonLoaderModule } from 'ngx-skeleton-loader';



@NgModule({
  declarations: [
    DashboardsComponent,
    DocComponent,
    DsidenavComponent,
    DformComponent,
    DtabsComponent,
    VideocallComponent,
    TranscriptionComponent,
    DialogComponent,
    DappointmentComponent,
    AboutComponent,
    ChatComponent,
    TodoComponent,




    
  ],
  imports: [
    CommonModule,
    DashboardsRoutingModule,
    MaterialModule,
    NgxSkeletonLoaderModule,
  
    
    NgxEchartsModule.forRoot({
      /**
       * This will import all modules from echarts.
       * If you only need custom modules,
       * please refer to [Custom Build] section.
       */
      echarts: () => import('echarts') // or import('./path-to-my-custom-echarts')
    }),

  ],
 
})
export class DashboardsModule { }
