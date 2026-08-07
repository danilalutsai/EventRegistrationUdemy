interface Animal {
  legs: number;
  eat(): void;
}

const legs = [12];

function optimistic(): void {
  for (let i = 0; i < legs.length; i++) {
    if (i > legs.length) return;
  }
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
