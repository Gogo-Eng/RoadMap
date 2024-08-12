function all_things() {
    this.number = 0;
    setTimeout(function() {
            this.number++;
            console.log(this.number);
    }.bind(this), 2000);
}

all_things();