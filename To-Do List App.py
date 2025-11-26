def todo_list_app():
    # Initialize tasks list
    tasks = []
    task_id_counter = 1
    
    print("=" * 50)
    print("          WELCOME TO YOUR TO-DO LIST")
    print("=" * 50)
    
    # Display menu
    def show_menu():
        print("\n📋 MENU OPTIONS:")
        print("1. Add new task")
        print("2. View all tasks")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. Show summary")
        print("6. Exit")
        print("-" * 30)
    
    # Add new task
    def add_task():
        nonlocal task_id_counter
        print("\n➕ ADD NEW TASK")
        description = input("Enter task description: ").strip()
        
        if not description:
            print("❌ Task description cannot be empty!")
            return
        
        print("\nPriority levels:")
        print("1 - High 🔴")
        print("2 - Medium 🟡") 
        print("3 - Low 🟢")
        
        try:
            priority_choice = int(input("Enter priority (1-3): "))
            if priority_choice == 1:
                priority = "High"
            elif priority_choice == 2:
                priority = "Medium"
            elif priority_choice == 3:
                priority = "Low"
            else:
                print("❌ Invalid priority! Setting to Medium.")
                priority = "Medium"
        except ValueError:
            print("❌ Invalid input! Setting priority to Medium.")
            priority = "Medium"
        
        task = {
            "id": task_id_counter,
            "description": description,
            "priority": priority,
            "completed": False
        }
        
        tasks.append(task)
        print(f"✅ Task '{description}' added successfully! (ID: {task_id_counter})")
        task_id_counter += 1
    
    # View all tasks
    def view_tasks():
        if not tasks:
            print("\n📭 No tasks in your to-do list!")
            return
        
        print("\n📋 YOUR TASKS:")
        print("-" * 60)
        print(f"{'ID':<4} {'Status':<12} {'Priority':<8} {'Description':<30}")
        print("-" * 60)
        
        for task in tasks:
            status = "✅ Done" if task["completed"] else "⏳ Pending"
            priority_icon = "🔴" if task["priority"] == "High" else "🟡" if task["priority"] == "Medium" else "🟢"
            print(f"{task['id']:<4} {status:<12} {priority_icon} {task['priority']:<6} {task['description']:<30}")
    
    # Mark task as complete
    def mark_complete():
        if not tasks:
            print("\n📭 No tasks to mark as complete!")
            return
        
        view_tasks()
        try:
            task_id = int(input("\nEnter task ID to mark as complete: "))
            
            for task in tasks:
                if task["id"] == task_id:
                    if not task["completed"]:
                        task["completed"] = True
                        print(f"✅ Task '{task['description']}' marked as complete!")
                    else:
                        print("ℹ️  Task is already completed!")
                    return
            
            print("❌ Task ID not found!")
            
        except ValueError:
            print("❌ Please enter a valid task ID!")
    
    # Delete task
    def delete_task():
        if not tasks:
            print("\n📭 No tasks to delete!")
            return
        
        view_tasks()
        try:
            task_id = int(input("\nEnter task ID to delete: "))
            
            for i, task in enumerate(tasks):
                if task["id"] == task_id:
                    deleted_task = tasks.pop(i)
                    print(f"🗑️  Task '{deleted_task['description']}' deleted successfully!")
                    return
            
            print("❌ Task ID not found!")
            
        except ValueError:
            print("❌ Please enter a valid task ID!")
    
    # Show summary
    def show_summary():
        if not tasks:
            print("\n📭 No tasks in your to-do list!")
            return
        
        completed = sum(1 for task in tasks if task["completed"])
        pending = len(tasks) - completed
        
        print("\n📊 SUMMARY:")
        print("-" * 30)
        print(f"Total tasks: {len(tasks)}")
        print(f"✅ Completed: {completed}")
        print(f"⏳ Pending: {pending}")
        
        if len(tasks) > 0:
            completion_rate = (completed / len(tasks)) * 100
            print(f"📈 Completion rate: {completion_rate:.1f}%")
        
        # Show high priority pending tasks
        high_priority_pending = [task for task in tasks if task["priority"] == "High" and not task["completed"]]
        if high_priority_pending:
            print(f"\n🔴 High priority pending tasks: {len(high_priority_pending)}")
            for task in high_priority_pending:
                print(f"   - {task['description']}")
    
    # Main program loop
    while True:
        show_menu()
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            show_summary()
        elif choice == "6":
            print("\n" + "=" * 50)
            print("           FINAL SUMMARY")
            print("=" * 50)
            show_summary()
            print("\n👋 Thank you for using the To-Do List App!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1-6.")

# Run the to-do list app
if __name__ == "__main__":
    todo_list_app()