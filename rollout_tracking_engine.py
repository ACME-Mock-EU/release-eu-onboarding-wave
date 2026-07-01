# Release 4.2 Rollout Tracking Engine
# Customer rollout management, milestone tracking, readiness assessment

import pandas as pd
from datetime import datetime

class RolloutTrackingEngine:
    def __init__(self):
        self.readiness_target = 0.85
        self.training_target = 0.90
        self.customers = ['BluePeak', 'Meridian', 'UrbanNest', 'NordForge', 'ClearWave', 'Helio']
        self.phases = ['Planning', 'UAT', 'Deployment', 'Post-Launch']
        self.go_live_date = '2026-07-14'
    
    def load_rollout_data(self, filepath):
        '''Load Release 4.2 EU onboarding rollout data'''
        df = pd.read_excel(filepath)
        return df
    
    def customer_readiness_analysis(self, rollout_df):
        '''Analyze readiness % by customer'''
        readiness = {}
        for customer in self.customers:
            cust_data = rollout_df[rollout_df['Customer'] == customer]
            if len(cust_data) > 0:
                readiness[customer] = {
                    'milestones': len(cust_data),
                    'avg_readiness': round(cust_data['Readiness %'].mean(), 3),
                    'min_readiness': round(cust_data['Readiness %'].min(), 3),
                    'max_readiness': round(cust_data['Readiness %'].max(), 3),
                    'status': 'On Track' if cust_data['Readiness %'].mean() > self.readiness_target else 'At Risk'
                }
        return readiness
    
    def training_readiness(self, rollout_df):
        '''Analyze training completion by customer'''
        training = {}
        for customer in self.customers:
            cust_data = rollout_df[rollout_df['Customer'] == customer]
            if len(cust_data) > 0:
                training[customer] = {
                    'avg_completion': round(cust_data['Training Completion %'].mean(), 3),
                    'target_completion': self.training_target,
                    'gap': round(self.training_target - cust_data['Training Completion %'].mean(), 3),
                    'status': 'On Track' if cust_data['Training Completion %'].mean() > self.training_target else 'Needs Completion'
                }
        return training
    
    def critical_blockers(self, rollout_df):
        '''Identify critical blockers'''
        blockers = []
        for idx, row in rollout_df.iterrows():
            blocker = row.get('Critical Blockers', '')
            if pd.notna(blocker) and blocker != '':
                blockers.append({
                    'customer': row['Customer'],
                    'phase': row['Phase'],
                    'blocker': blocker,
                    'milestone': row['Milestone'],
                    'dependency': row.get('Blocking Dependency', '')
                })
        return blockers
    
    def phase_distribution(self, rollout_df):
        '''Distribution of milestones by phase'''
        phase_dist = {}
        for phase in self.phases:
            phase_data = rollout_df[rollout_df['Phase'] == phase]
            phase_dist[phase] = {
                'count': len(phase_data),
                'pct': round((len(phase_data) / len(rollout_df)) * 100, 1),
                'avg_readiness': round(phase_data['Readiness %'].mean(), 3),
                'avg_training': round(phase_data['Training Completion %'].mean(), 3)
            }
        return phase_dist
    
    def go_live_confidence(self, rollout_df):
        '''Calculate go-live confidence score'''
        avg_readiness = rollout_df['Readiness %'].mean()
        avg_training = rollout_df['Training Completion %'].mean()
        blockers_count = len(rollout_df[rollout_df['Critical Blockers'].notna()])
        
        confidence_score = (avg_readiness * 0.4 + avg_training * 0.4 + max(0, 1 - (blockers_count / len(rollout_df))) * 0.2)
        
        if confidence_score > 0.85:
            status = 'High Confidence'
        elif confidence_score > 0.75:
            status = 'Moderate Confidence'
        else:
            status = 'At Risk'
        
        return {
            'confidence_score': round(confidence_score, 3),
            'status': status,
            'go_live_date': self.go_live_date,
            'blockers_count': blockers_count
        }

if __name__ == "__main__":
    engine = RolloutTrackingEngine()
    print("Rollout Tracking Engine v1.0 initialized")
    print("Release 4.2: 6 customers, 50 milestones, July 14 go-live")
