//https://leetcode.com/problems/can-make-palindrome-from-substring
//1177. Can Make Palindrome from Substring
//Difficulty: Medium
//Tags: String, Hash Table

// Key Concepts:
// Palindrome: A string that reads the same forward and backward, like "racecar" or "madam."
// Odd and Even Character Counts: To form a palindrome:
// If the length of the string is even, every character must appear an even number of times.
// If the length is odd, only one character can appear an odd number of times (this will be the middle character), while all others must appear an even number of times.
// Given this, for any substring to be rearranged into a palindrome:

// We need to count how many characters appear an odd number of times.
// If the number of characters with odd counts is small enough, we can make the string a palindrome by replacing some of those odd-count characters with other characters. The number of replacements allowed is given by k.
// How the Solution Works:
// Prefix Array: The solution uses a prefix array to efficiently count how many times each character appears up to a certain index in the string.
// prefix[i] contains a frequency count of all characters in the substring s[0...i-1].
// To find the frequency of each character in a specific substring s[lo...hi], you can subtract prefix[lo] from prefix[hi+1].

// Odd Count Calculation:
// For each query, we extract the character counts for the substring and check how many characters appear an odd number of times.

// Replacement Calculation:
// If there are odd characters with odd counts in the substring, then we need at least (odd - 1) / 2 replacements to convert them into a palindrome. The formula used is:
//     odd≤2𝑘+(sum%2)
// This formula checks whether we can handle all odd characters by using at most k replacements.


// KAUNIK
class Solution {
public:
    vector<bool> canMakePaliQueries(string s, vector<vector<int>>& queries) {
        vector<bool> ret;
        vector<vector<int>> prefix;
        vector<int> temp(26, 0);
        prefix.push_back(temp);
        for(int i=0; i<s.length(); i++)
        {
            temp[s[i]-'a']++;
            prefix.push_back(temp);
        }
        for(int i=0; i<queries.size(); i++)
        {
            int hi = queries[i][1], lo = queries[i][0], k = queries[i][2];
            vector<int> sub = prefix[hi+1];
            int odd=0, sum=hi-lo+1;
            for(int j=0; j<26; j++)
            {
                sub[j] = sub[j] - prefix[lo][j];
                odd+=sub[j]%2;
            }
            bool t = (odd <= k*2 + sum%2);
            ret.push_back(t);
        }
        return ret;
    }
};