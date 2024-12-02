/**
 * @param {string} sentence
 * @param {string} searchWord
 * @return {number}
 */
var isPrefixOfWord = function(sentence, searchWord) {
    const words = sentence.split(" ");
    let n = words.length;

    for (let i = 0; i < n; i++){
        if(words[i].startsWith(searchWord)){
            return i + 1;
        }
    }

    return -1;
};