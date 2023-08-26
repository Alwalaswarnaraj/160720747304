#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!pip install Flask


# In[4]:


from flask import Flask, request, jsonify


# In[5]:


app=Flask(__name__)


# In[9]:


@app.route('/add',methods=['post'])
def add_number():
    data=request.get_json()
    num1=data.get('num1')
    num2=data.get('num2')
    result=num1+num2
    return jsonify({'result':result})


# In[10]:


@app.route('/substract',methods=['post'])
def substract_number():
    data=request.get_json()
    num1=data.get('num1')
    num2=data.get('num2')
    result=num1+num2
    return jsonify({'result':result})


# In[12]:


if __name__== '__main__':
    app.run(debug=True)


# In[13]:


python app.py


# In[ ]:




