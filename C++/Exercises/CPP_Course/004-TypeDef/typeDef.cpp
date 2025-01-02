#include <iostream>
#include <vector>
#include <string>

int ComplexExample() {
	typedef std::vector<std::pair<std::string, int>> pairlist_t;
	
	pairlist_t pairlist;

	// '.push_back' appends values to a list in the "Vector" library.
	pairlist.push_back({"Alice", 30});
	pairlist.push_back({"Bob", 25});
	pairlist.push_back({"Charlie", 35});

	for (const auto& pair : pairlist) {
		std::cout << pair.first << ": " << pair.second << std::endl;
	}

	return 0;
}

int SimpleExample() {
	typedef std::string text_t;
	typedef int number_t;

	// Variable behaves like normal string.
	std::string firstName1 = "Steven";
	int age_1 = 38;
	std::cout << firstName1 << std::endl;
	std::cout << "Age: " << age_1 << std::endl;

	// This variable also behaves like a string, but uses 'text_t' typedef.
	text_t firstName2 = "Joshua";
	number_t age_2 = 25;
	std::cout << firstName2 << std::endl;
	std::cout << "Age: " << age_2 << std::endl;

	return 0;
}

int UsingExample() {
	using text_t = std::string;

	text_t name = "Charlie";

	std::cout << name << std::endl;	

	return 0;
}


int main() {
	ComplexExample();
	SimpleExample();
	UsingExample();
	return 0;
}