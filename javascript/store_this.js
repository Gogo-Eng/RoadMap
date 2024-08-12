function myFunc(name) {
    this.myVar = 0;
    this.name = name
    const self = this;
    setTimeout(function() {
      self.myVar++;
      console.log(self.myVar); // This will print 1
    }, 0);
  }
  
  const instance = new myFunc("Gogo");
  console.log(instance.name)