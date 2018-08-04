
# coding: utf-8

# In[1]:


import os
import math
import pandas as pd


# In[2]:


path = './docs'


# In[3]:


for index_number in range(100):
	index_number_string = str(index_number)

	# In[5]:


	def read_file(fname):
		print(fname)
		with open(os.path.join(path, fname)) as doc:
			text = doc.read()
			return text.lower() 


	# In[6]:


	docs = {os.path.splitext(fname)[0]: read_file(fname) for fname in list(os.walk(path))[0][2]} 


	# In[7]:


	def tokenize(document): 
		return document.split()


	# In[8]:


	def tf_raw(documents): 
		table = {}
		for doc in documents: 
			tf = {}
			for word in tokenize(documents[doc]): 
				if word in tf: 
					tf[word] += 1
				else: 
					tf[word] = 1
			table[doc] = tf
		return pd.DataFrame(table)


	# In[9]:


	tf_raw_ = tf_raw(docs)
	# tf_raw_.head(100)


	# In[10]:


	ans1 = list(map(lambda l, r: l + ":" + str(r), list(tf_raw_.count().index), list(tf_raw_.count().values)))
	ans1


	# In[11]:


	# def log_norm(n):
	#     return math.log10(1+n)
	def log_norm(n):
		if n <= 0: 
			return 0
		else:
			return 1 + math.log10(n)


	# In[12]:


	tf_log_norm_ = tf_raw_.applymap(log_norm)
	# tf_log_norm_.head(100)


	# In[13]:


	ans2 = [
		col + ":" + 
		tf_log_norm_[col].dropna().index[index_number] + "," +
		str(tf_log_norm_[col].dropna()[index_number]) 
		for col in tf_log_norm_.columns.values
	]
	ans2


	# In[14]:


	def idf_func(n, nt):
		return math.log10(n/nt)


	# In[15]:


	idf_ = tf_raw_.apply(lambda a: idf_func(len(a), a.count()), axis=1)


	# In[16]:


	ans3 = [
		col + ":" + 
    	tf_log_norm_[col].dropna().index[index_number] + "," +
    	str(idf_[tf_log_norm_[col].dropna().index[index_number]]) 
    	for col in tf_log_norm_.columns.values
	]
	ans3


	# In[17]:


	tf_idf_ = tf_log_norm_.fillna(0).rmul(idf_, axis='index')


	# $$TFIDF = (1 + \log f_{t,d})\times \log\frac{N}{n_t}$$

	# In[18]:


	ans4 = [
		col + ":" + 
		",".join(tf_idf_[col].nlargest(10).index.values.tolist())
		for col in tf_idf_.columns
	]
	ans4


	# In[19]:


	answer = "\n".join([index_number_string, "1", *ans1, "", "2", *ans2, "", "3", *ans3, "", "4", *ans4])
	# answer = "\r\n".join([index_number_string, "1", *ans1, "", "2", *ans2, "", "3", *ans3, "", "4", *ans4])
	# The sample answer.txt file has Windows line endings. (That won't probably matter.) Safety first. 


	# In[20]:


	with open('./out/' + index_number_string + '.txt', 'w+') as outfile:
		outfile.write(answer)

