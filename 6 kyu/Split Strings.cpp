#include <string>
#include <vector>

std::vector<std::string> solution(const std::string &s) {
  std::vector<std::string> ans;
  std::string copy = s;
  if (s.size() %2 == 1)
    copy += "_";
  
  
  for (size_t i = 0, count = 0; count < copy.size()/2; i += 2, ++count)
    ans.push_back(copy.substr(i, 2));
  
  return ans;
}