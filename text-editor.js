const text_editor = {
    text: "",
    append(s) {
        this.text = this.text.concat(s);
    },
    revert_append(s) {
        this.del(s.length);
    },
    del(i) {
        this.text = this.text.slice(0, i * -1);
    },
    print(i) {
        //console.log(this.text.charAt(i - 1));
        console.log(this.text);
    }
};

text_editor.append("abcd");
text_editor.append("xy");
text_editor.print();
text_editor.revert_append("xy");
//text_editor.del(1);
text_editor.print();
