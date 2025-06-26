class Solution {
public:
    string generateTag(string caption) {
        vector<string> words;
        string word = "";
        
        for (char c : caption) {
            if (c == ' ') {
                if (!word.empty()) {
                    words.push_back(word);
                    word = "";
                }
            } else {
                word += c;
            }
        }
        if (!word.empty()) words.push_back(word);
        
        string tag = "#";
        for (int i = 0; i < words.size(); i++) {
            string current = words[i];
            for (char& ch : current) ch = tolower(ch);
            if (i > 0 && !current.empty()) {
                current[0] = toupper(current[0]);
            }
            tag += current;
        }

        if (tag.size() > 100) {
            tag = tag.substr(0, 100);
        }
        // Ensure the tag does not end with a space
        if (!tag.empty() && tag.back() == ' ') {
            tag.pop_back();
        }
        return tag;
    }
};
