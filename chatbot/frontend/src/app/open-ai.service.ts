import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class OpenAIService {
  constructor(private http: HttpClient) {}

  getData(input: string): Observable<any> {
    const prompt = { "prompt" : input};
    return this.http.post(
      'http://localhost:5000/ask/', prompt,
      { responseType: 'json' }
    );
  }
}
