import { Component, ViewChild, ElementRef } from '@angular/core';
import { OpenAIService } from './open-ai.service';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'CoreGPT.UI';
  searchTxtVal: string[] = [];
  output: string[] = [];
  showOutput: boolean = false;
  isLoading: boolean = false;
  count: number = 0;
  nameControl = new FormControl('')

  constructor(private service: OpenAIService) {
    this.searchTxtVal = Array(100).fill("")
    this.output = Array(100).fill("")
  }

  async handleKeyDown(event: KeyboardEvent) {

    if (!event.shiftKey && event.keyCode === 13) {
      if(this.count == 100) {
        this.searchTxtVal = Array(100).fill("")
        this.output = Array(100).fill("")
      }
      this.isLoading = true;
      await this.service.getData(this.searchTxtVal[this.count]).subscribe((data) => {
        this.output[this.count] = (data["message"]);
        this.showOutput = true;
        this.isLoading = false;
        this.count++;
      });
    }
  }
}
