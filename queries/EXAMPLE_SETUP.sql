CREATE TABLE files (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    file_type TEXT NOT NULL,
    size BIGINT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT NOW(),
    modified TIMESTAMP NOT NULL DEFAULT NOW(),
    location TEXT NOT NULL
);


INSERT INTO files (name, file_type, size, created, modified, location) VALUES
('nov_report_01.pdf', 'pdf', 120000, '2025-11-01 09:15:00', '2025-11-01 09:15:00', '/docs/reports'),
('nov_report_02.pdf', 'pdf', 95000, '2025-11-03 14:32:00', '2025-11-03 14:32:00', '/docs/reports'),
('profile_nov.png', 'png', 56000, '2025-11-04 11:20:00', '2025-11-04 11:20:00', '/images/users'),
('logo.png', 'png', 56000, '2025-11-04 11:20:00', '2025-11-04 11:20:00', '/images/users'),
('data_export_nov.csv', 'csv', 1280000, '2025-11-05 08:00:00', '2025-11-05 08:00:00', '/exports'),
('presentation_nov.pptx', 'pptx', 3800000, '2025-11-10 10:45:30', '2025-11-10 11:00:00', '/docs/presentations'),
('nov_backup.zip', 'zip', 15000000, '2025-11-12 02:15:00', '2025-11-12 02:15:00', '/backups'),
('meeting_notes_nov.md', 'md', 16000, '2025-11-15 18:22:00', '2025-11-15 18:50:00', '/docs/notes'),
('system_log_nov.txt', 'txt', 8000, '2025-11-18 23:55:00', '2025-11-19 00:10:00', '/logs/system'),
('video_intro_nov.mp4', 'mp4', 45000000, '2025-11-25 18:22:00', '2025-11-25 18:22:00', '/videos'),
('training_data.csv', 'txt', 500000, '2025-11-12 02:15:00', '2025-11-12 02:15:00', '/training_data.csv');

SELECT * FROM files;
