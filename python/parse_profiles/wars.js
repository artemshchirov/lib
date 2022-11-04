function anagrams(word, words) {
    return words.map((w, i) => {
        w.filter((l, i) => l.sort() === word.sort()[i]);
    }).length > 0;
}

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) // => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) // => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy', 'lacer']) // => []