interface Animal {
  legs: number;
  eat(): void;
}

class Dog implements Animal {
  legs: number;

  constructor(legs: number) {
    this.legs = 4000;
  }
  
  eat(): void {
    console.log('Eating...');
  }
}

const foo = new Dog(4);
foo.eat();
