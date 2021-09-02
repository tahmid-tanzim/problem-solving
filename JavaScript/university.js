const fs = require('fs');
const old_university = [
  {
    "model": "profile.organization",
    "pk": 1,
    "fields": {
      "name_in_english": "Bangladesh Agricultural University",
      "type": "Educational Institution",
      "established_year": 1961
    }
  },
  {
    "model": "profile.organization",
    "pk": 2,
    "fields": {
      "name_in_english": "Bangabandhu Sheikh Mujibur Rahman Agricultural University",
      "type": "Educational Institution",
      "established_year": 1998
    }
  },
  {
    "model": "profile.organization",
    "pk": 3,
    "fields": {
      "name_in_english": "Sher-e-Bangla Agricultural University",
      "type": "Educational Institution",
      "established_year": 2001
    }
  },
  {
    "model": "profile.organization",
    "pk": 4,
    "fields": {
      "name_in_english": "Chittagong Veterinary and Animal Sciences University",
      "type": "Educational Institution",
      "established_year": 2006
    }
  },
  {
    "model": "profile.organization",
    "pk": 5,
    "fields": {
      "name_in_english": "Sylhet Agricultural University",
      "type": "Educational Institution",
      "established_year": 2006
    }
  },
  {
    "model": "profile.organization",
    "pk": 6,
    "fields": {
      "name_in_english": "Khulna Agricultural University",
      "type": "Educational Institution",
      "established_year": 2019
    }
  },
  {
    "model": "profile.organization",
    "pk": 7,
    "fields": {
      "name_in_english": "Habiganj Agricultural University",
      "type": "Educational Institution",
      "established_year": 2020
    }
  },
  {
    "model": "profile.organization",
    "pk": 8,
    "fields": {
      "name_in_english": "Bangladesh University of Engineering & Technology",
      "type": "Educational Institution",
      "established_year": 1962
    }
  },
  {
    "model": "profile.organization",
    "pk": 9,
    "fields": {
      "name_in_english": "Chittagong University of Engineering & Technology",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 10,
    "fields": {
      "name_in_english": "Rajshahi University of Engineering & Technology",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 11,
    "fields": {
      "name_in_english": "Khulna University of Engineering & Technology",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 12,
    "fields": {
      "name_in_english": "Dhaka University of Engineering & Technology",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 13,
    "fields": {
      "name_in_english": "University of Dhaka",
      "type": "Educational Institution",
      "established_year": 1921
    }
  },
  {
    "model": "profile.organization",
    "pk": 14,
    "fields": {
      "name_in_english": "University of Rajshahi",
      "type": "Educational Institution",
      "established_year": 1953
    }
  },
  {
    "model": "profile.organization",
    "pk": 15,
    "fields": {
      "name_in_english": "University of Chittagong",
      "type": "Educational Institution",
      "established_year": 1966
    }
  },
  {
    "model": "profile.organization",
    "pk": 16,
    "fields": {
      "name_in_english": "Jahangirnagar University",
      "type": "Educational Institution",
      "established_year": 1970
    }
  },
  {
    "model": "profile.organization",
    "pk": 17,
    "fields": {
      "name_in_english": "Islamic University, Bangladesh",
      "type": "Educational Institution",
      "established_year": 1979
    }
  },
  {
    "model": "profile.organization",
    "pk": 18,
    "fields": {
      "name_in_english": "Khulna University",
      "type": "Educational Institution",
      "established_year": 1991
    }
  },
  {
    "model": "profile.organization",
    "pk": 19,
    "fields": {
      "name_in_english": "Jagannath University",
      "type": "Educational Institution",
      "established_year": 2005
    }
  },
  {
    "model": "profile.organization",
    "pk": 20,
    "fields": {
      "name_in_english": "Jatiya Kabi Kazi Nazrul Islam University",
      "type": "Educational Institution",
      "established_year": 2006
    }
  },
  {
    "model": "profile.organization",
    "pk": 21,
    "fields": {
      "name_in_english": "Comilla University",
      "type": "Educational Institution",
      "established_year": 2006
    }
  },
  {
    "model": "profile.organization",
    "pk": 22,
    "fields": {
      "name_in_english": "Begum Rokeya University",
      "type": "Educational Institution",
      "established_year": 2008
    }
  },
  {
    "model": "profile.organization",
    "pk": 23,
    "fields": {
      "name_in_english": "Bangladesh University of Professionals",
      "type": "Educational Institution",
      "established_year": 2008
    }
  },
  {
    "model": "profile.organization",
    "pk": 24,
    "fields": {
      "name_in_english": "University of Barisal",
      "type": "Educational Institution",
      "established_year": 2011
    }
  },
  {
    "model": "profile.organization",
    "pk": 25,
    "fields": {
      "name_in_english": "Rabindra University, Bangladesh",
      "type": "Educational Institution",
      "established_year": 2017
    }
  },
  {
    "model": "profile.organization",
    "pk": 26,
    "fields": {
      "name_in_english": "Sheikh Hasina University",
      "type": "Educational Institution",
      "established_year": 2018
    }
  },
  {
    "model": "profile.organization",
    "pk": 27,
    "fields": {
      "name_in_english": "Bangabandhu Sheikh Mujibur Rahman University",
      "type": "Educational Institution",
      "established_year": 2020
    }
  },
  {
    "model": "profile.organization",
    "pk": 28,
    "fields": {
      "name_in_english": "Bangabandhu Sheikh Mujib Medical University",
      "type": "Educational Institution",
      "established_year": 1998
    }
  },
  {
    "model": "profile.organization",
    "pk": 29,
    "fields": {
      "name_in_english": "Rajshahi Medical University",
      "type": "Educational Institution",
      "established_year": 2017
    }
  },
  {
    "model": "profile.organization",
    "pk": 30,
    "fields": {
      "name_in_english": "Chittagong Medical University",
      "type": "Educational Institution",
      "established_year": 2017
    }
  },
  {
    "model": "profile.organization",
    "pk": 31,
    "fields": {
      "name_in_english": "Sylhet Medical University",
      "type": "Educational Institution",
      "established_year": 2018
    }
  },
  {
    "model": "profile.organization",
    "pk": 32,
    "fields": {
      "name_in_english": "Sheikh Hasina Medical University",
      "type": "Educational Institution",
      "established_year": 2020
    }
  },
  {
    "model": "profile.organization",
    "pk": 33,
    "fields": {
      "name_in_english": "Shahjalal University of Science and Technology",
      "type": "Educational Institution",
      "established_year": 1986
    }
  },
  {
    "model": "profile.organization",
    "pk": 34,
    "fields": {
      "name_in_english": "Hajee Mohammad Danesh Science & Technology University",
      "type": "Educational Institution",
      "established_year": 1999
    }
  },
  {
    "model": "profile.organization",
    "pk": 35,
    "fields": {
      "name_in_english": "Mawlana Bhashani Science and Technology University",
      "type": "Educational Institution",
      "established_year": 1999
    }
  },
  {
    "model": "profile.organization",
    "pk": 36,
    "fields": {
      "name_in_english": "Patuakhali Science and Technology University",
      "type": "Educational Institution",
      "established_year": 2000
    }
  },
  {
    "model": "profile.organization",
    "pk": 37,
    "fields": {
      "name_in_english": "Noakhali Science and Technology University",
      "type": "Educational Institution",
      "established_year": 2006
    }
  },
  {
    "model": "profile.organization",
    "pk": 38,
    "fields": {
      "name_in_english": "Jashore University of Science and Technology",
      "type": "Educational Institution",
      "established_year": 2007
    }
  },
  {
    "model": "profile.organization",
    "pk": 39,
    "fields": {
      "name_in_english": "Pabna University of Science and Technology",
      "type": "Educational Institution",
      "established_year": 2008
    }
  },
  {
    "model": "profile.organization",
    "pk": 40,
    "fields": {
      "name_in_english": "Bangabandhu Sheikh Mujibur Rahman Science and Technology University",
      "type": "Educational Institution",
      "established_year": 2011
    }
  },
  {
    "model": "profile.organization",
    "pk": 41,
    "fields": {
      "name_in_english": "Rangamati Science and Technology University",
      "type": "Educational Institution",
      "established_year": 2014
    }
  },
  {
    "model": "profile.organization",
    "pk": 42,
    "fields": {
      "name_in_english": "Bangamata Sheikh Fojilatunnesa Mujib Science & Technology University",
      "type": "Educational Institution",
      "established_year": 2018
    }
  },
  {
    "model": "profile.organization",
    "pk": 43,
    "fields": {
      "name_in_english": "Chandpur Science and Technology University",
      "type": "Educational Institution",
      "established_year": 2020
    }
  },
  {
    "model": "profile.organization",
    "pk": 44,
    "fields": {
      "name_in_english": "Sunamganj Science and Technology University",
      "type": "Educational Institution",
      "established_year": 2020
    }
  },
  {
    "model": "profile.organization",
    "pk": 45,
    "fields": {
      "name_in_english": "Bogura Science and Technology University",
      "type": "Educational Institution",
      "established_year": 2020
    }
  },
  {
    "model": "profile.organization",
    "pk": 46,
    "fields": {
      "name_in_english": "Lakshmipur Science and Technology University",
      "type": "Educational Institution",
      "established_year": 2020
    }
  },
  {
    "model": "profile.organization",
    "pk": 47,
    "fields": {
      "name_in_english": "Bangabandhu Sheikh Mujibur Rahman Digital University",
      "type": "Educational Institution",
      "established_year": 2018
    }
  },
  {
    "model": "profile.organization",
    "pk": 48,
    "fields": {
      "name_in_english": "Bangladesh University of Textiles",
      "type": "Educational Institution",
      "established_year": 2010
    }
  },
  {
    "model": "profile.organization",
    "pk": 49,
    "fields": {
      "name_in_english": "Bangabandhu Sheikh Mujibur Rahman Maritime University",
      "type": "Educational Institution",
      "established_year": 2013
    }
  },
  {
    "model": "profile.organization",
    "pk": 50,
    "fields": {
      "name_in_english": "Bangabandhu Sheikh Mujibur Rahman Aviation and Aerospace University",
      "type": "Educational Institution",
      "established_year": 2019
    }
  },
  {
    "model": "profile.organization",
    "pk": 51,
    "fields": {
      "name_in_english": "Bangladesh Open University",
      "type": "Educational Institution",
      "established_year": 1992
    }
  },
  {
    "model": "profile.organization",
    "pk": 52,
    "fields": {
      "name_in_english": "National University of Bangladesh",
      "type": "Educational Institution",
      "established_year": 1992
    }
  },
  {
    "model": "profile.organization",
    "pk": 53,
    "fields": {
      "name_in_english": "Islamic Arabic University",
      "type": "Educational Institution",
      "established_year": 2013
    }
  },
  {
    "model": "profile.organization",
    "pk": 54,
    "fields": {
      "name_in_english": "International University of Business Agriculture and Technology",
      "type": "Educational Institution",
      "established_year": 1991
    }
  },
  {
    "model": "profile.organization",
    "pk": 55,
    "fields": {
      "name_in_english": "North South University",
      "type": "Educational Institution",
      "established_year": 1992
    }
  },
  {
    "model": "profile.organization",
    "pk": 56,
    "fields": {
      "name_in_english": "University of Science & Technology Chittagong",
      "type": "Educational Institution",
      "established_year": 1992
    }
  },
  {
    "model": "profile.organization",
    "pk": 57,
    "fields": {
      "name_in_english": "Central Women's University",
      "type": "Educational Institution",
      "established_year": 1993
    }
  },
  {
    "model": "profile.organization",
    "pk": 58,
    "fields": {
      "name_in_english": "Independent University, Bangladesh",
      "type": "Educational Institution",
      "established_year": 1993
    }
  },
  {
    "model": "profile.organization",
    "pk": 59,
    "fields": {
      "name_in_english": "American International University-Bangladesh",
      "type": "Educational Institution",
      "established_year": 1994
    }
  },
  {
    "model": "profile.organization",
    "pk": 60,
    "fields": {
      "name_in_english": "Ahsanullah University of Science and Technology",
      "type": "Educational Institution",
      "established_year": 1995
    }
  },
  {
    "model": "profile.organization",
    "pk": 61,
    "fields": {
      "name_in_english": "Dhaka International University",
      "type": "Educational Institution",
      "established_year": 1995
    }
  },
  {
    "model": "profile.organization",
    "pk": 62,
    "fields": {
      "name_in_english": "International Islamic University, Chittagong",
      "type": "Educational Institution",
      "established_year": 1995
    }
  },
  {
    "model": "profile.organization",
    "pk": 63,
    "fields": {
      "name_in_english": "Asian University of Bangladesh",
      "type": "Educational Institution",
      "established_year": 1996
    }
  },
  {
    "model": "profile.organization",
    "pk": 64,
    "fields": {
      "name_in_english": "East West University",
      "type": "Educational Institution",
      "established_year": 1996
    }
  },
  {
    "model": "profile.organization",
    "pk": 65,
    "fields": {
      "name_in_english": "Gono Bishwabidyalay",
      "type": "Educational Institution",
      "established_year": 1996
    }
  },
  {
    "model": "profile.organization",
    "pk": 66,
    "fields": {
      "name_in_english": "People's University of Bangladesh",
      "type": "Educational Institution",
      "established_year": 1996
    }
  },
  {
    "model": "profile.organization",
    "pk": 67,
    "fields": {
      "name_in_english": "Queens University",
      "type": "Educational Institution",
      "established_year": 1996
    }
  },
  {
    "model": "profile.organization",
    "pk": 68,
    "fields": {
      "name_in_english": "University of Asia Pacific (Bangladesh)",
      "type": "Educational Institution",
      "established_year": 1996
    }
  },
  {
    "model": "profile.organization",
    "pk": 69,
    "fields": {
      "name_in_english": "BGMEA University of Fashion & Technology",
      "type": "Educational Institution",
      "established_year": 1999
    }
  },
  {
    "model": "profile.organization",
    "pk": 70,
    "fields": {
      "name_in_english": "Chittagong Independent University (CIU)",
      "type": "Educational Institution",
      "established_year": 1999
    }
  },
  {
    "model": "profile.organization",
    "pk": 71,
    "fields": {
      "name_in_english": "Bangladesh University",
      "type": "Educational Institution",
      "established_year": 2001
    }
  },
  {
    "model": "profile.organization",
    "pk": 72,
    "fields": {
      "name_in_english": "BGC Trust University Bangladesh",
      "type": "Educational Institution",
      "established_year": 2001
    }
  },
  {
    "model": "profile.organization",
    "pk": 73,
    "fields": {
      "name_in_english": "BRAC University",
      "type": "Educational Institution",
      "established_year": 2001
    }
  },
  {
    "model": "profile.organization",
    "pk": 74,
    "fields": {
      "name_in_english": "Manarat International University",
      "type": "Educational Institution",
      "established_year": 2001
    }
  },
  {
    "model": "profile.organization",
    "pk": 75,
    "fields": {
      "name_in_english": "Premier University, Chittagong",
      "type": "Educational Institution",
      "established_year": 2001
    }
  },
  {
    "model": "profile.organization",
    "pk": 76,
    "fields": {
      "name_in_english": "Pundra University of Science and Technology",
      "type": "Educational Institution",
      "established_year": 2001
    }
  },
  {
    "model": "profile.organization",
    "pk": 77,
    "fields": {
      "name_in_english": "Southern University, Bangladesh",
      "type": "Educational Institution",
      "established_year": 2001
    }
  },
  {
    "model": "profile.organization",
    "pk": 78,
    "fields": {
      "name_in_english": "Sylhet International University",
      "type": "Educational Institution",
      "established_year": 2001
    }
  },
  {
    "model": "profile.organization",
    "pk": 79,
    "fields": {
      "name_in_english": "City University, Bangladesh",
      "type": "Educational Institution",
      "established_year": 2002
    }
  },
  {
    "model": "profile.organization",
    "pk": 80,
    "fields": {
      "name_in_english": "Daffodil International University",
      "type": "Educational Institution",
      "established_year": 2002
    }
  },
  {
    "model": "profile.organization",
    "pk": 81,
    "fields": {
      "name_in_english": "Green University of Bangladesh",
      "type": "Educational Institution",
      "established_year": 2002
    }
  },
  {
    "model": "profile.organization",
    "pk": 82,
    "fields": {
      "name_in_english": "IBAIS University",
      "type": "Educational Institution",
      "established_year": 2002
    }
  },
  {
    "model": "profile.organization",
    "pk": 83,
    "fields": {
      "name_in_english": "Leading University",
      "type": "Educational Institution",
      "established_year": 2002
    }
  },
  {
    "model": "profile.organization",
    "pk": 84,
    "fields": {
      "name_in_english": "Northern University, Bangladesh",
      "type": "Educational Institution",
      "established_year": 2002
    }
  },
  {
    "model": "profile.organization",
    "pk": 85,
    "fields": {
      "name_in_english": "Prime University",
      "type": "Educational Institution",
      "established_year": 2002
    }
  },
  {
    "model": "profile.organization",
    "pk": 86,
    "fields": {
      "name_in_english": "Southeast University",
      "type": "Educational Institution",
      "established_year": 2002
    }
  },
  {
    "model": "profile.organization",
    "pk": 87,
    "fields": {
      "name_in_english": "Stamford University Bangladesh",
      "type": "Educational Institution",
      "established_year": 2002
    }
  },
  {
    "model": "profile.organization",
    "pk": 88,
    "fields": {
      "name_in_english": "State University of Bangladesh",
      "type": "Educational Institution",
      "established_year": 2002
    }
  },
  {
    "model": "profile.organization",
    "pk": 89,
    "fields": {
      "name_in_english": "University of Development Alternative",
      "type": "Educational Institution",
      "established_year": 2002
    }
  },
  {
    "model": "profile.organization",
    "pk": 90,
    "fields": {
      "name_in_english": "Bangladesh University of Business and Technology",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 91,
    "fields": {
      "name_in_english": "Eastern University, Bangladesh",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 92,
    "fields": {
      "name_in_english": "Metropolitan University",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 93,
    "fields": {
      "name_in_english": "Millennium University",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 94,
    "fields": {
      "name_in_english": "Presidency University",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 95,
    "fields": {
      "name_in_english": "Primeasia University",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 96,
    "fields": {
      "name_in_english": "Royal University of Dhaka",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 97,
    "fields": {
      "name_in_english": "Shanto-Mariam University of Creative Technology",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 98,
    "fields": {
      "name_in_english": "United International University",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 99,
    "fields": {
      "name_in_english": "University of Information Technology and Sciences",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 100,
    "fields": {
      "name_in_english": "University of South Asia, Bangladesh",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 101,
    "fields": {
      "name_in_english": "Uttara University",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 102,
    "fields": {
      "name_in_english": "Victoria University of Bangladesh",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 103,
    "fields": {
      "name_in_english": "World University of Bangladesh",
      "type": "Educational Institution",
      "established_year": 2003
    }
  },
  {
    "model": "profile.organization",
    "pk": 104,
    "fields": {
      "name_in_english": "Atish Dipankar University of Science and Technology",
      "type": "Educational Institution",
      "established_year": 2004
    }
  },
  {
    "model": "profile.organization",
    "pk": 105,
    "fields": {
      "name_in_english": "University of Liberal Arts Bangladesh",
      "type": "Educational Institution",
      "established_year": 2004
    }
  },
  {
    "model": "profile.organization",
    "pk": 106,
    "fields": {
      "name_in_english": "Asa University Bangladesh",
      "type": "Educational Institution",
      "established_year": 2006
    }
  },
  {
    "model": "profile.organization",
    "pk": 107,
    "fields": {
      "name_in_english": "Bangladesh Islami University",
      "type": "Educational Institution",
      "established_year": 2006
    }
  },
  {
    "model": "profile.organization",
    "pk": 108,
    "fields": {
      "name_in_english": "East Delta University",
      "type": "Educational Institution",
      "established_year": 2006
    }
  },
  {
    "model": "profile.organization",
    "pk": 109,
    "fields": {
      "name_in_english": "Britannia University",
      "type": "Educational Institution",
      "established_year": 2010
    }
  },
  {
    "model": "profile.organization",
    "pk": 110,
    "fields": {
      "name_in_english": "Feni University",
      "type": "Educational Institution",
      "established_year": 2010
    }
  },
  {
    "model": "profile.organization",
    "pk": 111,
    "fields": {
      "name_in_english": "Khwaja Yunus Ali University",
      "type": "Educational Institution",
      "established_year": 2010
    }
  },
  {
    "model": "profile.organization",
    "pk": 112,
    "fields": {
      "name_in_english": "Bangladesh University of Health Sciences",
      "type": "Educational Institution",
      "established_year": 2012
    }
  },
  {
    "model": "profile.organization",
    "pk": 113,
    "fields": {
      "name_in_english": "European University of Bangladesh",
      "type": "Educational Institution",
      "established_year": 2012
    }
  },
  {
    "model": "profile.organization",
    "pk": 114,
    "fields": {
      "name_in_english": "First Capital University Of Bangladesh",
      "type": "Educational Institution",
      "established_year": 2012
    }
  },
  {
    "model": "profile.organization",
    "pk": 115,
    "fields": {
      "name_in_english": "Hamdard University Bangladesh",
      "type": "Educational Institution",
      "established_year": 2012
    }
  },
  {
    "model": "profile.organization",
    "pk": 116,
    "fields": {
      "name_in_english": "Ishakha International University",
      "type": "Educational Institution",
      "established_year": 2012
    }
  },
  {
    "model": "profile.organization",
    "pk": 117,
    "fields": {
      "name_in_english": "North East University Bangladesh",
      "type": "Educational Institution",
      "established_year": 2012
    }
  },
  {
    "model": "profile.organization",
    "pk": 118,
    "fields": {
      "name_in_english": "North Western University, Bangladesh",
      "type": "Educational Institution",
      "established_year": 2012
    }
  },
  {
    "model": "profile.organization",
    "pk": 119,
    "fields": {
      "name_in_english": "Port City International University",
      "type": "Educational Institution",
      "established_year": 2012
    }
  },
  {
    "model": "profile.organization",
    "pk": 120,
    "fields": {
      "name_in_english": "Sonargaon University",
      "type": "Educational Institution",
      "established_year": 2012
    }
  },
  {
    "model": "profile.organization",
    "pk": 121,
    "fields": {
      "name_in_english": "Varendra University",
      "type": "Educational Institution",
      "established_year": 2012
    }
  },
  {
    "model": "profile.organization",
    "pk": 122,
    "fields": {
      "name_in_english": "Z H Sikder University of Science & Technology",
      "type": "Educational Institution",
      "established_year": 2012
    }
  },
  {
    "model": "profile.organization",
    "pk": 123,
    "fields": {
      "name_in_english": "Rajshahi Science & Technology University",
      "type": "Educational Institution",
      "established_year": 2013
    }
  },
  {
    "model": "profile.organization",
    "pk": 124,
    "fields": {
      "name_in_english": "Coxs Bazar International University",
      "type": "Educational Institution",
      "established_year": 2013
    }
  },
  {
    "model": "profile.organization",
    "pk": 125,
    "fields": {
      "name_in_english": "Exim Bank Agricultural University Bangladesh",
      "type": "Educational Institution",
      "established_year": 2013
    }
  },
  {
    "model": "profile.organization",
    "pk": 126,
    "fields": {
      "name_in_english": "Fareast International University",
      "type": "Educational Institution",
      "established_year": 2013
    }
  },
  {
    "model": "profile.organization",
    "pk": 127,
    "fields": {
      "name_in_english": "German University Bangladesh",
      "type": "Educational Institution",
      "established_year": 2013
    }
  },
  {
    "model": "profile.organization",
    "pk": 128,
    "fields": {
      "name_in_english": "Notre Dame University Bangladesh",
      "type": "Educational Institution",
      "established_year": 2013
    }
  },
  {
    "model": "profile.organization",
    "pk": 129,
    "fields": {
      "name_in_english": "Sheikh Fazilatunnesa Mujib University",
      "type": "Educational Institution",
      "established_year": 2013
    }
  },
  {
    "model": "profile.organization",
    "pk": 130,
    "fields": {
      "name_in_english": "Times University, Bangladesh",
      "type": "Educational Institution",
      "established_year": 2013
    }
  },
  {
    "model": "profile.organization",
    "pk": 131,
    "fields": {
      "name_in_english": "Bangladesh Army International University of Science & Technology",
      "type": "Educational Institution",
      "established_year": 2015
    }
  },
  {
    "model": "profile.organization",
    "pk": 132,
    "fields": {
      "name_in_english": "Bangladesh Army University of Engineering & Technology",
      "type": "Educational Institution",
      "established_year": 2015
    }
  },
  {
    "model": "profile.organization",
    "pk": 133,
    "fields": {
      "name_in_english": "Bangladesh Army University of Science and Technology",
      "type": "Educational Institution",
      "established_year": 2015
    }
  },
  {
    "model": "profile.organization",
    "pk": 134,
    "fields": {
      "name_in_english": "Canadian University of Bangladesh",
      "type": "Educational Institution",
      "established_year": 2015
    }
  },
  {
    "model": "profile.organization",
    "pk": 135,
    "fields": {
      "name_in_english": "CCN University of Science & Technology",
      "type": "Educational Institution",
      "established_year": 2015
    }
  },
  {
    "model": "profile.organization",
    "pk": 136,
    "fields": {
      "name_in_english": "Global University Bangladesh",
      "type": "Educational Institution",
      "established_year": 2015
    }
  },
  {
    "model": "profile.organization",
    "pk": 137,
    "fields": {
      "name_in_english": "NPI University of Bangladesh",
      "type": "Educational Institution",
      "established_year": 2015
    }
  },
  {
    "model": "profile.organization",
    "pk": 138,
    "fields": {
      "name_in_english": "Rabindra Maitree University",
      "type": "Educational Institution",
      "established_year": 2015
    }
  },
  {
    "model": "profile.organization",
    "pk": 139,
    "fields": {
      "name_in_english": "The International University of Scholars",
      "type": "Educational Institution",
      "established_year": 2015
    }
  },
  {
    "model": "profile.organization",
    "pk": 140,
    "fields": {
      "name_in_english": "University of Creative Technology Chittagong",
      "type": "Educational Institution",
      "established_year": 2015
    }
  },
  {
    "model": "profile.organization",
    "pk": 141,
    "fields": {
      "name_in_english": "Anwer Khan Modern University",
      "type": "Educational Institution",
      "established_year": 2016
    }
  },
  {
    "model": "profile.organization",
    "pk": 142,
    "fields": {
      "name_in_english": "Central University of Science and Technology",
      "type": "Educational Institution",
      "established_year": 2016
    }
  },
  {
    "model": "profile.organization",
    "pk": 143,
    "fields": {
      "name_in_english": "University of Global Village",
      "type": "Educational Institution",
      "established_year": 2016
    }
  },
  {
    "model": "profile.organization",
    "pk": 144,
    "fields": {
      "name_in_english": "Z.N.R.F. University of Management Sciences",
      "type": "Educational Institution",
      "established_year": 2018
    }
  },
  {
    "model": "profile.organization",
    "pk": 145,
    "fields": {
      "name_in_english": "Islamic University of Technology",
      "type": "Educational Institution",
      "established_year": 1981
    }
  },
  {
    "model": "profile.organization",
    "pk": 146,
    "fields": {
      "name_in_english": "Asian University for Women",
      "type": "Educational Institution",
      "established_year": 2008
    }
  }
];

const new_university = old_university.map(x => {
    return {
        "model": x['model'],
        "pk": x['pk'],
        "fields": {
          "name_in_english": x['fields']['name_in_english'],
          "type": x['fields']['type']
        }
      };
});

// stringify JSON Object
var jsonContent = JSON.stringify(new_university, null, 2);

fs.writeFile("university.json", jsonContent, 'utf8', function (err) {
    if (err) {
        console.log("An error occured while writing JSON Object to File.");
        return console.log(err);
    }

    console.log("University JSON file has been saved.");
});