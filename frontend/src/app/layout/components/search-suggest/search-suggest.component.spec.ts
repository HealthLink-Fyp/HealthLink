import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchSuggestComponent } from './search-suggest.component';

describe('SearchSuggestComponent', () => {
  let component: SearchSuggestComponent;
  let fixture: ComponentFixture<SearchSuggestComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SearchSuggestComponent]
    });
    fixture = TestBed.createComponent(SearchSuggestComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
