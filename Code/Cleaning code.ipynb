{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9fb76763",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8e841dd0",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv(\"Message_Data_Spam.csv\",encoding='Latin-1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5afd9567",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>v1</th>\n",
       "      <th>v2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ham</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ham</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>spam</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ham</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ham</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5567</th>\n",
       "      <td>spam</td>\n",
       "      <td>This is the 2nd time we have tried 2 contact u...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5568</th>\n",
       "      <td>ham</td>\n",
       "      <td>Will Ì_ b going to esplanade fr home?</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5569</th>\n",
       "      <td>ham</td>\n",
       "      <td>Pity, * was in mood for that. So...any other s...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5570</th>\n",
       "      <td>ham</td>\n",
       "      <td>The guy did some bitching but I acted like i'd...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5571</th>\n",
       "      <td>ham</td>\n",
       "      <td>Rofl. Its true to its name</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5572 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        v1                                                 v2\n",
       "0      ham  Go until jurong point, crazy.. Available only ...\n",
       "1      ham                      Ok lar... Joking wif u oni...\n",
       "2     spam  Free entry in 2 a wkly comp to win FA Cup fina...\n",
       "3      ham  U dun say so early hor... U c already then say...\n",
       "4      ham  Nah I don't think he goes to usf, he lives aro...\n",
       "...    ...                                                ...\n",
       "5567  spam  This is the 2nd time we have tried 2 contact u...\n",
       "5568   ham              Will Ì_ b going to esplanade fr home?\n",
       "5569   ham  Pity, * was in mood for that. So...any other s...\n",
       "5570   ham  The guy did some bitching but I acted like i'd...\n",
       "5571   ham                         Rofl. Its true to its name\n",
       "\n",
       "[5572 rows x 2 columns]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b0f0a39a",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.rename(columns={\"v1\":\"Target\",\"v2\":\"Text\"},inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0856fca6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Target</th>\n",
       "      <th>Text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ham</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ham</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>spam</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ham</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ham</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5567</th>\n",
       "      <td>spam</td>\n",
       "      <td>This is the 2nd time we have tried 2 contact u...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5568</th>\n",
       "      <td>ham</td>\n",
       "      <td>Will Ì_ b going to esplanade fr home?</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5569</th>\n",
       "      <td>ham</td>\n",
       "      <td>Pity, * was in mood for that. So...any other s...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5570</th>\n",
       "      <td>ham</td>\n",
       "      <td>The guy did some bitching but I acted like i'd...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5571</th>\n",
       "      <td>ham</td>\n",
       "      <td>Rofl. Its true to its name</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5572 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Target                                               Text\n",
       "0       ham  Go until jurong point, crazy.. Available only ...\n",
       "1       ham                      Ok lar... Joking wif u oni...\n",
       "2      spam  Free entry in 2 a wkly comp to win FA Cup fina...\n",
       "3       ham  U dun say so early hor... U c already then say...\n",
       "4       ham  Nah I don't think he goes to usf, he lives aro...\n",
       "...     ...                                                ...\n",
       "5567   spam  This is the 2nd time we have tried 2 contact u...\n",
       "5568    ham              Will Ì_ b going to esplanade fr home?\n",
       "5569    ham  Pity, * was in mood for that. So...any other s...\n",
       "5570    ham  The guy did some bitching but I acted like i'd...\n",
       "5571    ham                         Rofl. Its true to its name\n",
       "\n",
       "[5572 rows x 2 columns]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2f702b43",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "403"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "48206cc8",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.drop_duplicates(inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a8e5f2b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Target</th>\n",
       "      <th>Text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ham</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ham</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>spam</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ham</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ham</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5567</th>\n",
       "      <td>spam</td>\n",
       "      <td>This is the 2nd time we have tried 2 contact u...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5568</th>\n",
       "      <td>ham</td>\n",
       "      <td>Will Ì_ b going to esplanade fr home?</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5569</th>\n",
       "      <td>ham</td>\n",
       "      <td>Pity, * was in mood for that. So...any other s...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5570</th>\n",
       "      <td>ham</td>\n",
       "      <td>The guy did some bitching but I acted like i'd...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5571</th>\n",
       "      <td>ham</td>\n",
       "      <td>Rofl. Its true to its name</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5169 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Target                                               Text\n",
       "0       ham  Go until jurong point, crazy.. Available only ...\n",
       "1       ham                      Ok lar... Joking wif u oni...\n",
       "2      spam  Free entry in 2 a wkly comp to win FA Cup fina...\n",
       "3       ham  U dun say so early hor... U c already then say...\n",
       "4       ham  Nah I don't think he goes to usf, he lives aro...\n",
       "...     ...                                                ...\n",
       "5567   spam  This is the 2nd time we have tried 2 contact u...\n",
       "5568    ham              Will Ì_ b going to esplanade fr home?\n",
       "5569    ham  Pity, * was in mood for that. So...any other s...\n",
       "5570    ham  The guy did some bitching but I acted like i'd...\n",
       "5571    ham                         Rofl. Its true to its name\n",
       "\n",
       "[5169 rows x 2 columns]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5ec48e05",
   "metadata": {},
   "outputs": [],
   "source": [
    "data['Target'] = data['Target'].replace(\"ham\",0)\n",
    "data['Target'] = data['Target'].replace(\"spam\",1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b3d5b64a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    4516\n",
       "1     653\n",
       "Name: Target, dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Target'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "a439d892",
   "metadata": {},
   "outputs": [],
   "source": [
    "# plt.pie(data['Target'].value_counts(),labels=['ham','spam'],autopct='%0.2f')\n",
    "# plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "7756bb43",
   "metadata": {},
   "outputs": [],
   "source": [
    "import nltk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "86c6bc36",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to\n",
      "[nltk_data]     C:\\Users\\Mi\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nltk.download(\"punkt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "c073eca1",
   "metadata": {},
   "outputs": [],
   "source": [
    "data['characters'] = data['Text'].apply(len)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "7eb3f631",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Target</th>\n",
       "      <th>Text</th>\n",
       "      <th>characters</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "      <td>111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "      <td>155</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "      <td>49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "      <td>61</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5567</th>\n",
       "      <td>1</td>\n",
       "      <td>This is the 2nd time we have tried 2 contact u...</td>\n",
       "      <td>161</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5568</th>\n",
       "      <td>0</td>\n",
       "      <td>Will Ì_ b going to esplanade fr home?</td>\n",
       "      <td>37</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5569</th>\n",
       "      <td>0</td>\n",
       "      <td>Pity, * was in mood for that. So...any other s...</td>\n",
       "      <td>57</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5570</th>\n",
       "      <td>0</td>\n",
       "      <td>The guy did some bitching but I acted like i'd...</td>\n",
       "      <td>125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5571</th>\n",
       "      <td>0</td>\n",
       "      <td>Rofl. Its true to its name</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5169 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Target                                               Text  characters\n",
       "0          0  Go until jurong point, crazy.. Available only ...         111\n",
       "1          0                      Ok lar... Joking wif u oni...          29\n",
       "2          1  Free entry in 2 a wkly comp to win FA Cup fina...         155\n",
       "3          0  U dun say so early hor... U c already then say...          49\n",
       "4          0  Nah I don't think he goes to usf, he lives aro...          61\n",
       "...      ...                                                ...         ...\n",
       "5567       1  This is the 2nd time we have tried 2 contact u...         161\n",
       "5568       0              Will Ì_ b going to esplanade fr home?          37\n",
       "5569       0  Pity, * was in mood for that. So...any other s...          57\n",
       "5570       0  The guy did some bitching but I acted like i'd...         125\n",
       "5571       0                         Rofl. Its true to its name          26\n",
       "\n",
       "[5169 rows x 3 columns]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "5d7fb2f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "data['words'] = data['Text'].apply(lambda x : len(nltk.word_tokenize(x)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "5987d28f",
   "metadata": {},
   "outputs": [],
   "source": [
    "data['sentences'] = data['Text'].apply(lambda x : len(nltk.sent_tokenize(x)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "e1310f0c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Target</th>\n",
       "      <th>Text</th>\n",
       "      <th>characters</th>\n",
       "      <th>words</th>\n",
       "      <th>sentences</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "      <td>111</td>\n",
       "      <td>24</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "      <td>29</td>\n",
       "      <td>8</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "      <td>155</td>\n",
       "      <td>37</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "      <td>49</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "      <td>61</td>\n",
       "      <td>15</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5567</th>\n",
       "      <td>1</td>\n",
       "      <td>This is the 2nd time we have tried 2 contact u...</td>\n",
       "      <td>161</td>\n",
       "      <td>35</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5568</th>\n",
       "      <td>0</td>\n",
       "      <td>Will Ì_ b going to esplanade fr home?</td>\n",
       "      <td>37</td>\n",
       "      <td>9</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5569</th>\n",
       "      <td>0</td>\n",
       "      <td>Pity, * was in mood for that. So...any other s...</td>\n",
       "      <td>57</td>\n",
       "      <td>15</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5570</th>\n",
       "      <td>0</td>\n",
       "      <td>The guy did some bitching but I acted like i'd...</td>\n",
       "      <td>125</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5571</th>\n",
       "      <td>0</td>\n",
       "      <td>Rofl. Its true to its name</td>\n",
       "      <td>26</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5169 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Target                                               Text  characters  \\\n",
       "0          0  Go until jurong point, crazy.. Available only ...         111   \n",
       "1          0                      Ok lar... Joking wif u oni...          29   \n",
       "2          1  Free entry in 2 a wkly comp to win FA Cup fina...         155   \n",
       "3          0  U dun say so early hor... U c already then say...          49   \n",
       "4          0  Nah I don't think he goes to usf, he lives aro...          61   \n",
       "...      ...                                                ...         ...   \n",
       "5567       1  This is the 2nd time we have tried 2 contact u...         161   \n",
       "5568       0              Will Ì_ b going to esplanade fr home?          37   \n",
       "5569       0  Pity, * was in mood for that. So...any other s...          57   \n",
       "5570       0  The guy did some bitching but I acted like i'd...         125   \n",
       "5571       0                         Rofl. Its true to its name          26   \n",
       "\n",
       "      words  sentences  \n",
       "0        24          2  \n",
       "1         8          2  \n",
       "2        37          2  \n",
       "3        13          1  \n",
       "4        15          1  \n",
       "...     ...        ...  \n",
       "5567     35          4  \n",
       "5568      9          1  \n",
       "5569     15          2  \n",
       "5570     27          1  \n",
       "5571      7          2  \n",
       "\n",
       "[5169 rows x 5 columns]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "6fb8f820",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Target</th>\n",
       "      <th>characters</th>\n",
       "      <th>words</th>\n",
       "      <th>sentences</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>5169.000000</td>\n",
       "      <td>5169.000000</td>\n",
       "      <td>5169.000000</td>\n",
       "      <td>5169.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>0.126330</td>\n",
       "      <td>78.977945</td>\n",
       "      <td>18.455794</td>\n",
       "      <td>1.965564</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.332253</td>\n",
       "      <td>58.236293</td>\n",
       "      <td>13.324758</td>\n",
       "      <td>1.448541</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>36.000000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>60.000000</td>\n",
       "      <td>15.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>117.000000</td>\n",
       "      <td>26.000000</td>\n",
       "      <td>2.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>910.000000</td>\n",
       "      <td>220.000000</td>\n",
       "      <td>38.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Target   characters        words    sentences\n",
       "count  5169.000000  5169.000000  5169.000000  5169.000000\n",
       "mean      0.126330    78.977945    18.455794     1.965564\n",
       "std       0.332253    58.236293    13.324758     1.448541\n",
       "min       0.000000     2.000000     1.000000     1.000000\n",
       "25%       0.000000    36.000000     9.000000     1.000000\n",
       "50%       0.000000    60.000000    15.000000     1.000000\n",
       "75%       0.000000   117.000000    26.000000     2.000000\n",
       "max       1.000000   910.000000   220.000000    38.000000"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "14401447",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot: xlabel='characters', ylabel='Count'>"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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68zJyTF+8pOfmNM333yzce21135jLStXrjS6du1qTo8bN8648cYbW+1/8803Gw899JDXvHnz5hmjRo3ymnfw4EFDklFcXNxqPc8995xx1VVXGQ0NDd9YJ4D2xZEdAD61Z88e1dfXa+TIka32GTRokPm+e/fukqTKykpJktvt1rx58zRw4EDFx8crOjpa7733nkpLS73WMWTIkLPWu27dOo0cOVI9evRQly5dNGHCBB07dkynTp2S9I8jOxdj+/bt+uCDDxQdHW2++vfvL0n64osvWq3n+9//vk6fPq0+ffpo8uTJevPNN82jVwA6FmEHgE9FRER8Y5/Q0FDzfVBQkKSvx/lI0rPPPqsXX3xRjz76qD744AMVFRUpOzv7rEG/UVFRXtMHDhzQbbfdpkGDBukPf/iDCgsLlZeXJ+kfA4YvpLYz1dbW6vbbb1dRUZHXa+/evbrppptarSclJUXFxcV65ZVXFBERoQcffFA33XSTGhsbL7oGAJeGsAPAp/r166eIiAjl5+e3aflPPvlEd9xxh+655x5dc8016tOnjz7//PNvXK6wsFAej0fPPfechg8frquuukpHjhzx6jNo0KDz1hUWFia32+0177rrrtOuXbvUq1cv9e3b1+t1ZsA5U0REhG6//Xa99NJL+vDDD1VQUKAdO3Z847YA8C3CDgCfCg8P16OPPqpHHnlEv/nNb/TFF19o06ZNWrJkyQUt369fP61du1YbN27Unj179KMf/UgVFRXfuFzfvn3V2Niol19+Wfv27dP//u//mgOXm82cOVNbt27Vgw8+qE8//VSfffaZFi1aZF5Z1atXL23evFkHDhzQ0aNH5fF4lJubq+PHj2vcuHHaunWrvvjiC7333nv64Q9/eFYwamnZsmVasmSJdu7cqX379un1119XRESE0tLSLuh7AOA7hB0APjd79mz95Cc/0Zw5czRgwADddddd5picbzJr1ixdd911ys7O1ogRI5SUlKQ777zzG5e75ppr9Pzzz+s///M/dfXVV+uNN97Q/PnzvfpcddVVev/997V9+3bdcMMNcjqd+tOf/iSbzSZJ+ulPf6qQkBBlZGSoW7duKi0tVXJysj755BO53W6NGjVKAwcO1LRp0xQXF6fg4Nb/hMbFxenVV1/VjTfeqEGDBmndunV655131LVr1wv6HgD4TpBhGIa/iwAAAGgvHNkBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACW9v8BCuE3fGABDAoAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.histplot(data[data['Target']==0]['characters'])\n",
    "sns.histplot(data[data['Target']==1]['characters'],color='red')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "9aa319ca",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Mi\\AppData\\Local\\Temp\\ipykernel_4976\\2578434383.py:1: FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.\n",
      "  sns.heatmap(data.corr(),annot=True)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot: >"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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Ksg3emWRa50B3t6ViIjUgnxX3Vd4ciUDzs7O700Inj59+kEBERERUdmSKxkICAiAsbFxacVCRERUPnCY4O369u0LKyur0oqFiIiofFCzZKDEVxNwvgAREVHlJPfVBERERJVeBVksSFlKnAxI1KzLhIiI1JiafeYpdAtjIiKiSk3NesPlvjcBERERVS7sGSAiIiqMwwRERERqTs2SAQ4TEBERqTn2DBARERXGSwuJiIjUmyDh1QRERESkRtgzQEREVJiaTSBkMkBERFSYms0Z4DABERGRmmPPABERUWFqNoGQyQAREVFhnDNARESk5tQsGeCcASIiIjXHngEiIqLC1OwWxkwGiIiICuMwAREREakT9gwQEREVxksLiYiI1BxXICQiIiJ1wp4BIiKiwjhMoBodXIapOgR641jkKlWHQG9I0hNVHQK9cbXNIlWHQGVI4NUEREREpE7KTc8AERFRucFhAiIiIjXHqwmIiIjUnERQ3ianFStWwNHREbq6unBzc8OlS5feWT84OBh16tSBnp4eHBwcMH78eLx+/VquYzIZICIiKie2b98OX19fzJw5ExEREWjcuDG8vLyQnJxcbP2tW7di6tSpmDlzJmJiYrB27Vps374dP/zwg1zHZTJARERUmESivE0OQUFB8PHxgbe3N+rXr4+VK1dCX18f69atK7b++fPn4eHhgf79+8PR0REdO3ZEv3793tubUBiTASIiosKUOEyQnZ2N58+fy2zZ2dlFDpmTk4Pw8HB4enpKyzQ0NODp6YkLFy4UG2aLFi0QHh4u/fC/e/cuDh06hM6dO8t1ukwGiIiISlFgYCCMjY1ltsDAwCL1UlNTkZ+fD2tra5lya2trJCYWv+ZI//79MXv2bLRs2RLa2tqoVasW2rZty2ECIiKiDyZIlLb5+fnh2bNnMpufn59Swjx16hTmz5+PX375BREREdizZw8OHjyIOXPmyNUOLy0kIiIqTInrDIjFYojF4vfWs7CwgKamJpKSkmTKk5KSYGNjU+w+M2bMwNdff42hQ4cCABo2bIisrCwMGzYM06ZNg4ZGyb7zs2eAiIioHNDR0YGrqytCQ0OlZRKJBKGhoXB3dy92n5cvXxb5wNfU1AQACELJExql9Azk5+cjOjoa1atXh6mpqTKaJCIiUhlV3ZvA19cXgwcPRrNmzdC8eXMEBwcjKysL3t7e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Nen7JS0tTWa/qKgotGvXDlWqVIGRkRFcXV1x5cqV0jz1UrNr1y40bNgQenp6MDc3h6enJ7KysgAAa9asQb169aCrq4u6devil19+ke73zzDbnj17in3/nDp1Ct7e3nj27FmRns3s7GxMnDgR9vb2MDAwgJubG06dOiVt+58ehSNHjqBevXowNDREp06dZL4sAcC6deukr6+trS1Gjx4tfS4jIwNDhw6FpaUljIyM8OmnnyIqKkr6fGV6DSs1gYT169cLxsbG0seRkZHCypUrhejoaCEuLk6YPn26oKurKzx48EBap3r16oKRkZGwaNEiIT4+XoiPjxfOnj0raGhoCAsXLhRiY2OFFStWCGZmZjJt//3334KRkZGwYcMG4c6dO8LRo0cFR0dHYdasWYIgCEJycrIAQFi/fr3w5MkTITk5uax+DR9s8uTJgqmpqbBhwwYhPj5eOHPmjLB69Wrh3r17AgChbt26wl9//SXExsYKX375pVC9enUhNzdXEARBePjwobBw4ULh6tWrwp07d4Sff/5Z0NTUFMLCwqTtt2nTRjA0NBQmTZok3Lp1S7h165YgCIKwZMkS4cSJE8K9e/eE0NBQoU6dOsKIESOk+129elUQi8XCiBEjhMjISOH69evCsmXLhJSUFCEjI0Nwd3cXfHx8hCdPnghPnjwR8vLyhPT0dMHS0lLw8/MTYmJihIiICKFDhw5Cu3bt3hnPzp07BSMjI+HQoUPCgwcPhLCwMGHVqlVl9AooT0ZGhqChoSFcvnxZEARBCA4OFiwsLAQ3NzdpHScnJ2H16tXClStXBA0NDWH27NlCbGyssH79ekFPT09Yv369tG5x75eLFy8KGhoawo8//ijExsYKS5cuFUxMTGTeLx999JEwcOBAISYmRoiLixN27NghREZGltWvQWkeP34saGlpCUFBQcK9e/eEa9euCStWrBBevHghbN68WbC1tRV2794t3L17V9i9e7dgZmYmbNiwQRAE4b3vn+zsbCE4OFgwMjKS/h9+8eKFIAiCMHToUKFFixbC33//LcTHxwsLFy4UxGKxEBcXJwhCwd8+bW1twdPTU7h8+bIQHh4u1KtXT+jfv7809l9++UXQ1dUVgoODhdjYWOHSpUvCkiVLpM97enoKXbt2FS5fvizExcUJEyZMEMzNzYW0tDRBECrPa1jZMRkQiiYDxfno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",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(data.corr(),annot=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "1d89d57d",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import string\n",
    "from nltk.stem.porter import PorterStemmer\n",
    "ps = PorterStemmer()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "e550ad8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package stopwords to\n",
      "[nltk_data]     C:\\Users\\Mi\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package stopwords is already up-to-date!\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nltk.download('stopwords')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "73f0278c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Transform_text(text):\n",
    "    text = text.lower()\n",
    "    text = nltk.word_tokenize(text)\n",
    "    L = []\n",
    "\n",
    "    for i in text:\n",
    "        if i.isalnum():\n",
    "            L.append(i)\n",
    "            \n",
    "    text = L[:]\n",
    "    L.clear()\n",
    "    \n",
    "    for i in text:\n",
    "        if i not in stopwords.words('english') and i not in string.punctuation:\n",
    "            L.append(i)\n",
    "            \n",
    "    text = L[:]\n",
    "    L.clear()\n",
    "    for i in text:\n",
    "        L.append(ps.stem(i)) \n",
    "        \n",
    "    return \" \".join(L)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "f36fd782",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hi harsh agraw danc'"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Transform_text(\"Hi This Is Harsh Agrawal&&&%%%  !!! Dances\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "75d80b0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "data['Transformed_text'] = data['Text'].apply(Transform_text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "39cca4b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Target</th>\n",
       "      <th>Text</th>\n",
       "      <th>characters</th>\n",
       "      <th>words</th>\n",
       "      <th>sentences</th>\n",
       "      <th>Transformed_text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "      <td>111</td>\n",
       "      <td>24</td>\n",
       "      <td>2</td>\n",
       "      <td>go jurong point crazi avail bugi n great world...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "      <td>29</td>\n",
       "      <td>8</td>\n",
       "      <td>2</td>\n",
       "      <td>ok lar joke wif u oni</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "      <td>155</td>\n",
       "      <td>37</td>\n",
       "      <td>2</td>\n",
       "      <td>free entri 2 wkli comp win fa cup final tkt 21...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "      <td>49</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "      <td>u dun say earli hor u c alreadi say</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "      <td>61</td>\n",
       "      <td>15</td>\n",
       "      <td>1</td>\n",
       "      <td>nah think goe usf live around though</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5567</th>\n",
       "      <td>1</td>\n",
       "      <td>This is the 2nd time we have tried 2 contact u...</td>\n",
       "      <td>161</td>\n",
       "      <td>35</td>\n",
       "      <td>4</td>\n",
       "      <td>2nd time tri 2 contact u pound prize 2 claim e...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5568</th>\n",
       "      <td>0</td>\n",
       "      <td>Will Ì_ b going to esplanade fr home?</td>\n",
       "      <td>37</td>\n",
       "      <td>9</td>\n",
       "      <td>1</td>\n",
       "      <td>b go esplanad fr home</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5569</th>\n",
       "      <td>0</td>\n",
       "      <td>Pity, * was in mood for that. So...any other s...</td>\n",
       "      <td>57</td>\n",
       "      <td>15</td>\n",
       "      <td>2</td>\n",
       "      <td>piti mood suggest</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5570</th>\n",
       "      <td>0</td>\n",
       "      <td>The guy did some bitching but I acted like i'd...</td>\n",
       "      <td>125</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>guy bitch act like interest buy someth els nex...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5571</th>\n",
       "      <td>0</td>\n",
       "      <td>Rofl. Its true to its name</td>\n",
       "      <td>26</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "      <td>rofl true name</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5169 rows × 6 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Target                                               Text  characters  \\\n",
       "0          0  Go until jurong point, crazy.. Available only ...         111   \n",
       "1          0                      Ok lar... Joking wif u oni...          29   \n",
       "2          1  Free entry in 2 a wkly comp to win FA Cup fina...         155   \n",
       "3          0  U dun say so early hor... U c already then say...          49   \n",
       "4          0  Nah I don't think he goes to usf, he lives aro...          61   \n",
       "...      ...                                                ...         ...   \n",
       "5567       1  This is the 2nd time we have tried 2 contact u...         161   \n",
       "5568       0              Will Ì_ b going to esplanade fr home?          37   \n",
       "5569       0  Pity, * was in mood for that. So...any other s...          57   \n",
       "5570       0  The guy did some bitching but I acted like i'd...         125   \n",
       "5571       0                         Rofl. Its true to its name          26   \n",
       "\n",
       "      words  sentences                                   Transformed_text  \n",
       "0        24          2  go jurong point crazi avail bugi n great world...  \n",
       "1         8          2                              ok lar joke wif u oni  \n",
       "2        37          2  free entri 2 wkli comp win fa cup final tkt 21...  \n",
       "3        13          1                u dun say earli hor u c alreadi say  \n",
       "4        15          1               nah think goe usf live around though  \n",
       "...     ...        ...                                                ...  \n",
       "5567     35          4  2nd time tri 2 contact u pound prize 2 claim e...  \n",
       "5568      9          1                              b go esplanad fr home  \n",
       "5569     15          2                                  piti mood suggest  \n",
       "5570     27          1  guy bitch act like interest buy someth els nex...  \n",
       "5571      7          2                                     rofl true name  \n",
       "\n",
       "[5169 rows x 6 columns]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d389f889",
   "metadata": {},
   "source": [
    "# "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "96569efb",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.feature_extraction.text import CountVectorizer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "d2003066",
   "metadata": {},
   "outputs": [],
   "source": [
    "cv = CountVectorizer()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "73314349",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = cv.fit_transform(data['Transformed_text']).toarray()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "a9c5a34d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5169, 6708)"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "e9ba770c",
   "metadata": {},
   "outputs": [],
   "source": [
    "y = data['Target']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "63318135",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn import metrics\n",
    "from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "af4660e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "96822548",
   "metadata": {},
   "outputs": [],
   "source": [
    "models = {\n",
    "    \"LogisticReg\":LogisticRegression(),\n",
    "    \"DecisionTree\":DecisionTreeClassifier(),\n",
    "    \"RandomForest\":RandomForestClassifier(),\n",
    "    \"AdaBoost\":AdaBoostClassifier(),\n",
    "    \"GredientBoost\":GradientBoostingClassifier()\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "5dde6d97",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LogisticReg\n",
      "Accuracy Score 0.9706109822119103\n",
      "Precision Score 0.9788732394366197\n",
      "DecisionTree\n",
      "Accuracy Score 0.9497293116782676\n",
      "Precision Score 0.8562091503267973\n",
      "RandomForest\n",
      "Accuracy Score 0.9644238205723125\n",
      "Precision Score 0.9923076923076923\n",
      "AdaBoost\n",
      "Accuracy Score 0.9574632637277649\n",
      "Precision Score 0.9219858156028369\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[41], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m name,model \u001b[38;5;129;01min\u001b[39;00m models\u001b[38;5;241m.\u001b[39mitems():\n\u001b[1;32m----> 2\u001b[0m     \u001b[43mmodel\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mfit\u001b[49m\u001b[43m(\u001b[49m\u001b[43mx_train\u001b[49m\u001b[43m,\u001b[49m\u001b[43my_train\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m      3\u001b[0m     y_pred \u001b[38;5;241m=\u001b[39m model\u001b[38;5;241m.\u001b[39mpredict(x_test)\n\u001b[0;32m      4\u001b[0m     \u001b[38;5;28mprint\u001b[39m(name)\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\ensemble\\_gb.py:538\u001b[0m, in \u001b[0;36mBaseGradientBoosting.fit\u001b[1;34m(self, X, y, sample_weight, monitor)\u001b[0m\n\u001b[0;32m    535\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_resize_state()\n\u001b[0;32m    537\u001b[0m \u001b[38;5;66;03m# fit the boosting stages\u001b[39;00m\n\u001b[1;32m--> 538\u001b[0m n_stages \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_fit_stages\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    539\u001b[0m \u001b[43m    \u001b[49m\u001b[43mX\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    540\u001b[0m \u001b[43m    \u001b[49m\u001b[43my\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    541\u001b[0m \u001b[43m    \u001b[49m\u001b[43mraw_predictions\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    542\u001b[0m \u001b[43m    \u001b[49m\u001b[43msample_weight\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    543\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_rng\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    544\u001b[0m \u001b[43m    \u001b[49m\u001b[43mX_val\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    545\u001b[0m \u001b[43m    \u001b[49m\u001b[43my_val\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    546\u001b[0m \u001b[43m    \u001b[49m\u001b[43msample_weight_val\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    547\u001b[0m \u001b[43m    \u001b[49m\u001b[43mbegin_at_stage\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    548\u001b[0m \u001b[43m    \u001b[49m\u001b[43mmonitor\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    549\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    551\u001b[0m \u001b[38;5;66;03m# change shape of arrays after fit (early-stopping or additional ests)\u001b[39;00m\n\u001b[0;32m    552\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m n_stages \u001b[38;5;241m!=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mestimators_\u001b[38;5;241m.\u001b[39mshape[\u001b[38;5;241m0\u001b[39m]:\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\ensemble\\_gb.py:615\u001b[0m, in \u001b[0;36mBaseGradientBoosting._fit_stages\u001b[1;34m(self, X, y, raw_predictions, sample_weight, random_state, X_val, y_val, sample_weight_val, begin_at_stage, monitor)\u001b[0m\n\u001b[0;32m    608\u001b[0m     old_oob_score \u001b[38;5;241m=\u001b[39m loss_(\n\u001b[0;32m    609\u001b[0m         y[\u001b[38;5;241m~\u001b[39msample_mask],\n\u001b[0;32m    610\u001b[0m         raw_predictions[\u001b[38;5;241m~\u001b[39msample_mask],\n\u001b[0;32m    611\u001b[0m         sample_weight[\u001b[38;5;241m~\u001b[39msample_mask],\n\u001b[0;32m    612\u001b[0m     )\n\u001b[0;32m    614\u001b[0m \u001b[38;5;66;03m# fit next stage of trees\u001b[39;00m\n\u001b[1;32m--> 615\u001b[0m raw_predictions \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_fit_stage\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    616\u001b[0m \u001b[43m    \u001b[49m\u001b[43mi\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    617\u001b[0m \u001b[43m    \u001b[49m\u001b[43mX\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    618\u001b[0m \u001b[43m    \u001b[49m\u001b[43my\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    619\u001b[0m \u001b[43m    \u001b[49m\u001b[43mraw_predictions\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    620\u001b[0m \u001b[43m    \u001b[49m\u001b[43msample_weight\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    621\u001b[0m \u001b[43m    \u001b[49m\u001b[43msample_mask\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    622\u001b[0m \u001b[43m    \u001b[49m\u001b[43mrandom_state\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    623\u001b[0m \u001b[43m    \u001b[49m\u001b[43mX_csc\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    624\u001b[0m \u001b[43m    \u001b[49m\u001b[43mX_csr\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    625\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    627\u001b[0m \u001b[38;5;66;03m# track deviance (= loss)\u001b[39;00m\n\u001b[0;32m    628\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m do_oob:\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\ensemble\\_gb.py:257\u001b[0m, in \u001b[0;36mBaseGradientBoosting._fit_stage\u001b[1;34m(self, i, X, y, raw_predictions, sample_weight, sample_mask, random_state, X_csc, X_csr)\u001b[0m\n\u001b[0;32m    254\u001b[0m     sample_weight \u001b[38;5;241m=\u001b[39m sample_weight \u001b[38;5;241m*\u001b[39m sample_mask\u001b[38;5;241m.\u001b[39mastype(np\u001b[38;5;241m.\u001b[39mfloat64)\n\u001b[0;32m    256\u001b[0m X \u001b[38;5;241m=\u001b[39m X_csr \u001b[38;5;28;01mif\u001b[39;00m X_csr \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;28;01melse\u001b[39;00m X\n\u001b[1;32m--> 257\u001b[0m \u001b[43mtree\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mfit\u001b[49m\u001b[43m(\u001b[49m\u001b[43mX\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mresidual\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43msample_weight\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43msample_weight\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcheck_input\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m)\u001b[49m\n\u001b[0;32m    259\u001b[0m \u001b[38;5;66;03m# update tree leaves\u001b[39;00m\n\u001b[0;32m    260\u001b[0m loss\u001b[38;5;241m.\u001b[39mupdate_terminal_regions(\n\u001b[0;32m    261\u001b[0m     tree\u001b[38;5;241m.\u001b[39mtree_,\n\u001b[0;32m    262\u001b[0m     X,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    269\u001b[0m     k\u001b[38;5;241m=\u001b[39mk,\n\u001b[0;32m    270\u001b[0m )\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\tree\\_classes.py:1247\u001b[0m, in \u001b[0;36mDecisionTreeRegressor.fit\u001b[1;34m(self, X, y, sample_weight, check_input)\u001b[0m\n\u001b[0;32m   1218\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mfit\u001b[39m(\u001b[38;5;28mself\u001b[39m, X, y, sample_weight\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m, check_input\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m):\n\u001b[0;32m   1219\u001b[0m     \u001b[38;5;124;03m\"\"\"Build a decision tree regressor from the training set (X, y).\u001b[39;00m\n\u001b[0;32m   1220\u001b[0m \n\u001b[0;32m   1221\u001b[0m \u001b[38;5;124;03m    Parameters\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   1244\u001b[0m \u001b[38;5;124;03m        Fitted estimator.\u001b[39;00m\n\u001b[0;32m   1245\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[1;32m-> 1247\u001b[0m     \u001b[38;5;28;43msuper\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mfit\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m   1248\u001b[0m \u001b[43m        \u001b[49m\u001b[43mX\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1249\u001b[0m \u001b[43m        \u001b[49m\u001b[43my\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1250\u001b[0m \u001b[43m        \u001b[49m\u001b[43msample_weight\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43msample_weight\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1251\u001b[0m \u001b[43m        \u001b[49m\u001b[43mcheck_input\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mcheck_input\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1252\u001b[0m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m   1253\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\tree\\_classes.py:379\u001b[0m, in \u001b[0;36mBaseDecisionTree.fit\u001b[1;34m(self, X, y, sample_weight, check_input)\u001b[0m\n\u001b[0;32m    368\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    369\u001b[0m     builder \u001b[38;5;241m=\u001b[39m BestFirstTreeBuilder(\n\u001b[0;32m    370\u001b[0m         splitter,\n\u001b[0;32m    371\u001b[0m         min_samples_split,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    376\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mmin_impurity_decrease,\n\u001b[0;32m    377\u001b[0m     )\n\u001b[1;32m--> 379\u001b[0m \u001b[43mbuilder\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mbuild\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mtree_\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mX\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43my\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43msample_weight\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    381\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mn_outputs_ \u001b[38;5;241m==\u001b[39m \u001b[38;5;241m1\u001b[39m \u001b[38;5;129;01mand\u001b[39;00m is_classifier(\u001b[38;5;28mself\u001b[39m):\n\u001b[0;32m    382\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mn_classes_ \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mn_classes_[\u001b[38;5;241m0\u001b[39m]\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "for name,model in models.items():\n",
    "    model.fit(x_train,y_train)\n",
    "    y_pred = model.predict(x_test)\n",
    "    print(name)\n",
    "    print(\"Accuracy Score\",metrics.accuracy_score(y_test,y_pred))\n",
    "    print(\"Precision Score\",metrics.precision_score(y_test,y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "949c3544",
   "metadata": {},
   "outputs": [],
   "source": [
    "# sns.heatmap(metrics.confusion_matrix(y_test,y_pred),annot=True,fmt = 'g')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a661a42",
   "metadata": {},
   "outputs": [],
   "source": [
    "# tn, fp, fn, tp = metrics.confusion_matrix(y_test,y_pred).ravel()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "61628287",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 226,
   "id": "05b194df",
   "metadata": {},
   "outputs": [],
   "source": [
    "pickle.dump(cv,open(\"Vector.pkl\",'wb'))\n",
    "pickle.dump(models['RandomForest'],open(\"Model.pkl\",'wb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 318,
   "id": "27b5a814",
   "metadata": {},
   "outputs": [],
   "source": [
    "pickle.dump(models['LogisticReg'],open(\"Model1.pkl\",'wb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e396fede",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9249f3d2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3cc20919",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "3896c44e",
   "metadata": {},
   "outputs": [],
   "source": [
    "vector = pickle.load(open(\"Vector.pkl\",'rb'))\n",
    "model = pickle.load(open(\"Model.pkl\",'rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "86152d5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "model1 = pickle.load(open(\"Model1.pkl\",'rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "968a3ad3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ffffffffff. Alright no way I can meet up with you sooner?\n"
     ]
    }
   ],
   "source": [
    "text = input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "33943119",
   "metadata": {},
   "outputs": [],
   "source": [
    "transform_text = Transform_text(text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "24e1f069",
   "metadata": {},
   "outputs": [],
   "source": [
    "Vector_input = vector.transform([transform_text])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "e9527c06",
   "metadata": {},
   "outputs": [],
   "source": [
    "result = model.predict(Vector_input)[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "71d2b1ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Not Spam\n"
     ]
    }
   ],
   "source": [
    "if result==1:\n",
    "    print(\"spam\")\n",
    "else:\n",
    "    print(\"Not Spam\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "42dcbf0a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
