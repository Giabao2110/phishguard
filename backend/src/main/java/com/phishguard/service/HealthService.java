package com.phishguard.service;

import com.phishguard.dto.HealthResponse;
import org.springframework.stereotype.Service;

@Service
public class HealthService {

    public HealthResponse getStatus() {
        return new HealthResponse("UP", "phishguard-backend");
    }
}
