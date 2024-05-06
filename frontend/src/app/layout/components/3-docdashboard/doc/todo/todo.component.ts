import { Component } from '@angular/core';

interface Task {
  text: string;
  done: boolean;
}

@Component({
  selector: 'app-todo',
  templateUrl: './todo.component.html',
  styleUrls: ['./todo.component.css']
})
export class TodoComponent {

  public tasks: Task[] = [];

  constructor() { }

  addTask(task: string) {
    if (task === "") return;
    this.tasks.push({
      text: task,
      done: false
    });
  }

  removeTask(task: Task) {
    this.tasks.splice(this.tasks.indexOf(task), 1);
  }

  toggle(task: Task) {
    task.done = !task.done;
  }
}