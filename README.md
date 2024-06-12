# Habitfit Tracker

Habitfit Tracker is an app designed to help you track your habits and improve your lifestyle. Whether you’re aiming to establish new habits or break old ones, Habitfit provides an intuitive and user-friendly interface to monitor your progress.
![image](https://github.com/2100032578cse/Habitfit/assets/99196826/9478d5b5-eaad-4764-aeaf-b9910e6c447d)

## Features

- **Habit Tracking:** Log your daily habits and activities effortlessly.
- **Progress Monitoring:** Visualize your progress over time.
- **Motivational Reminders:** Receive timely reminders to stay on track.
- **Customizable Goals:** Set personalized goals for each habit.
- **User-Friendly Design:** Enjoy a seamless experience with our intuitive interface.

Stay motivated, build positive routines, and achieve your lifestyle goals with Habitfit Tracker!

 ## Technologies

- **Front-end:** HTML, CSS, JavaScript and Bootstrap
- **Back-end:** Flask
- **Database:** SQLite/MYSQL
- **Hosting:** pythonanywhere
  
  ![image](https://github.com/2100032578cse/Habitfit/assets/99196826/fcb46188-cce7-4db8-bec0-5babf965df45)

  ## User flow
  # User Registration and Login

- Users register using their name, email, and password.
- Users log in using their email and password.
- Upon login, the user’s role is checked to determine their permissions.
  ![image](https://github.com/2100032578cse/Habitfit/assets/99196826/ddfc7e16-c8de-42e4-9fdc-32bd0ac77c9a)


# Activity Management

- Users can add general activities.
- Daily activities are tracked using the `user_daily_activity` table.
  ![image](https://github.com/2100032578cse/Habitfit/assets/99196826/42835ba9-08c0-497a-8184-53c4ca4781df)

# Health Metrics Management



- Users update their health metrics such as blood pressure, height, and weight.
- BMI is calculated and stored.

  ![image](https://github.com/2100032578cse/Habitfit/assets/99196826/3bdb67a2-207b-4aaa-9bf9-0648179e9b57)


  # Challenges and Solutions

Here are the challenges we encountered during our project development, along with the solutions we implemented:

1. **Performance Under Heavy User Load**:
    - **Challenge**: Ensuring the app's performance when handling a large number of users simultaneously.
    - **Solution**: We optimized the database queries used by fine-tuning indexes, caching frequently accessed data, and implementing efficient query execution plans.

2. **Compatibility Issues with Flask Extensions**:
    - **Challenge**: Some Flask extensions (such as Bootstrap) were not compatible with our development workspace.
    - **Solution**: To maintain functionality, we explored alternative approaches, such as using different libraries or customizing existing components.
  
      # Landpage look
      ![image](https://github.com/2100032578cse/Habitfit/assets/99196826/e415910a-8e13-4923-8111-f28c372536a7)



  # Learnings and Technical Interests

Through this project, we gained valuable insights in full-stack development, particularly with Flask and front-end technologies.
We also learned about the importance of user experience design and how it impacts user retention and satisfaction.
This project has sparked a deeper interest in health tech and the potential it holds for improving lives, as it was fulfilling our needs as well.


Link to deployed project : https://sandrinerw.pythonanywhere.com/

