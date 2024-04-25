import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DsidenavComponent } from './dsidenav.component';

describe('DsidenavComponent', () => {
  let component: DsidenavComponent;
  let fixture: ComponentFixture<DsidenavComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DsidenavComponent]
    });
    fixture = TestBed.createComponent(DsidenavComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
