from apscheduler.schedulers.background import BackgroundScheduler

def schedule_script_updates():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_scripts, 'interval', hours=24)  # Update scripts daily
    scheduler.start()

if __name__ == '__main__':
    update_scripts()  # Initial update
    schedule_script_updates()
    main()
