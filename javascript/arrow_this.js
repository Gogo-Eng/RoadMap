function myFunc() {
  this.myVar = 0;
  setTimeout(() => {
    this.myVar++;
    console.log(this.myVar); // This will print 1
  }, 0);
}

const instance = new myFunc();
