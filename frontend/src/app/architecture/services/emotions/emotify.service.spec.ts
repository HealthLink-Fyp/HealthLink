import { TestBed } from '@angular/core/testing';

import { EmotifyService } from './emotify.service';

describe('EmotifyService', () => {
  let service: EmotifyService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EmotifyService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
