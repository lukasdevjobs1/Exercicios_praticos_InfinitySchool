# To-Do List Application - Version 1.0

import streamlit as st
import pandas as pd

# init session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = pd.DataFrame(columns=['Tarefa', 'Complete'])

def add_task(task):
    """Add a new task to the DataFrame"""
    if task.strip():
        new_task = pd.DataFrame([{'Tarefa': task, 'Complete': False}])
        st.session_state.tasks = pd.concat([st.session_state.tasks, new_task], ignore_index=True)
        return True
    return False

def remove_task(index):
    """Remove task by index"""
    if 0 <= index < len(st.session_state.tasks):
        st.session_state.tasks = st.session_state.tasks.drop(index).reset_index(drop=True)
    if st.button('Mark as Completed'):
        if mark_completed(complete_index):
            st.button('✅ Concluir', key=f'complete_{index}', on_click=mark_completed, args=(index,))
        st.button('❌ Remover', key=f'remove_{index}', on_click=remove_task, args=(index,))
        return True
    return False
def mark_completed(index):
    """Mark a task as complete"""
    if 0 <= index < len(st.session_state.tasks):
        st.session_state.tasks.loc[index, 'Complete'] = True
        return True
    return False

# Interface principal
st.title('📝 To-Do List')

# Add new task
task_input = st.text_input('Add a new task:')

if st.button('To add Task'):
    if add_task(task_input):
        st.success('Task added successfully!')
        
    else:
        st.error('Please add valid task')

# Show tasks
if not st.session_state.tasks.empty:
    st.subheader('Task List')
    st.dataframe(st.session_state.tasks)
    
    if len(st.session_state.tasks) > 0:
        remove_index = st.selectbox('Select the task to remove:', st.session_state.tasks.index)
        if st.button('Task removed'):
            if remove_task(remove_index):
                st.success('Task removed')
                
    
    if len(st.session_state.tasks) > 0:
        complete_index = st.selectbox('Select the task to complete:', st.session_state.tasks.index)
        if st.button('Mark as Completed'):
            if mark_completed(complete_index):
                st.success('Task marked as completed!')
                
else:
    st.info('No tasks in the list.')
# Removed unnecessary else block
st.info('No tasks in the list.')
st.success('Task removed!')

    
    # Estatístics Section
total_tasks = len(st.session_state.tasks)
completed_tasks = len(st.session_state.tasks[st.session_state.tasks['Complete'] == True])
pending_tasks = total_tasks - completed_tasks

st.subheader('📊 Estatístics')
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total", total_tasks)
with col2:
    st.metric("Completed", completed_tasks)
with col3:
    st.metric("Pending", pending_tasks)

# Options to clear all tasks
if not st.session_state.tasks.empty:
    st.subheader('🧹 Manage List')
    if st.button('🗑️ Clear All Tasks', type='secondary'):
        st.session_state.tasks = pd.DataFrame(columns=['Task', 'Complete'])
      
        